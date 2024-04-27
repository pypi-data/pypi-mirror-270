import asyncio
import logging.config
import os

import click
import yaml
from prompt_toolkit import HTML, PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

from airda.agent import DataAgentKey
from airda.agent.agent import DataAgent
from airda.agent.env import DataAgentEnv
from airda.agent.exception.already_exists_error import AlreadyExistsError
from airda.agent.planner.data_agent_planner_params import DataAgentPlannerParams
from airda.agent.storage import StorageKey
from airda.agent.storage.entity.datasource import Datasource, Kind
from airda.agent.storage.repositories.datasource_repository import DatasourceRepository
from airda.connector.mysql import MysqlConnector
from airda.server.agent_server import DataAgentServer

style = Style.from_dict(
    {
        "prompt": "bold #a68a0d",
        "output": "#3993d4",
        "success": "#4fc414",
        "error": "#f0524f bold",
    }
)
session = PromptSession(style=style)

bindings = KeyBindings()
user_path = "~/.airda"
config_path = os.path.expanduser(user_path)
os.makedirs(config_path, exist_ok=True)
env_path = config_path + "/" + ".env"
log_path = config_path + "/" + "log_config.yml"
DataAgentEnv(env_path)
log_config = {}
try:
    with open(log_path, "r") as f:
        log_config = yaml.safe_load(f)
        logging.config.dictConfig(log_config)
except Exception:
    pass


def output_colored_text(text, style_class, line_break=True):
    end = ""
    if line_break:
        end = "\n"
    print_formatted_text(HTML(f"<{style_class}>{text}</{style_class}>"), end=end, style=style)


@bindings.add("c-c")
def _(event):
    event.app.exit()


# command cli
@click.group()
def main():
    pass


@main.group()
def run():
    pass


@run.command()
@click.option(
    "-n",
    "--name",
    type=str,
    required=True,
    help="数据源名称",
)
def cli(name: str):
    context = DataAgent().run()
    while True:
        user_input = session.prompt("输入你的问题:")
        if user_input.lower() == "exit":
            break
        params = {"question": user_input, "datasource_name": name}
        pipeline = context.plan(DataAgentPlannerParams(**params))

        async def execute():
            async for item in pipeline.execute():
                if item == "[DONE]":
                    output_colored_text("", "output", False)
                else:
                    output_colored_text(item, "output", False)
            session.output.write("\n")
            session.output.flush()

        asyncio.run(execute())


# command server
@run.command()
@click.option(
    "-p",
    "--port",
    type=int,
    required=True,
    help="服务端口号",
)
def server(port: int):
    data_agent_server = DataAgentServer(port=port)
    data_agent_server.run_server()
    pass


# command datasource
@main.group()
def datasource():
    pass


@datasource.command(help="添加数据源")
@click.option(
    "-n",
    "--name",
    type=str,
    required=True,
    help="数据源名称",
)
@click.option(
    "-h",
    "--host",
    type=str,
    required=True,
    help="数据源的地址",
)
@click.option(
    "-p",
    "--port",
    type=int,
    required=True,
    help="数据源的端口",
)
@click.option(
    "-k",
    "--kind",
    type=str,
    required=True,
    help="数据源种类目前只支持: [{}]".format(Kind.MYSQL.name),
)
@click.option(
    "-d",
    "--database",
    type=str,
    required=True,
    help="数据库名称",
)
@click.option(
    "-u",
    "--username",
    type=str,
    required=False,
    help="数据源的用户名",
)
@click.option(
    "-w",
    "--password",
    type=str,
    required=False,
    help="数据源的密码",
)
def add(name: str, host: str, port: int, database: str, kind: str, username: str, password: str):
    kind = Kind.getKind(kind)
    if kind is None:
        output_colored_text(f"不支持的数据源类型[{kind}], PS: 支持类型: [{Kind.MYSQL.value}]", "error")
        return
    context = DataAgent(DataAgentKey.STORAGE).run()
    datasource_repository = context.get_repository(StorageKey.DATASOURCE).convert(
        DatasourceRepository
    )
    try:
        datasource_repository.add(
            Datasource(
                name=name,
                host=host,
                port=port,
                database=database,
                kind=kind,
                username=username,
                password=password,
            )
        )
        output_colored_text("执行成功", "success")
    except AlreadyExistsError:
        output_colored_text(f"执行失败, [{name}]数据源已存在", "error")


@datasource.command(help="同步数据源的表字段信息并进行向量化")
@click.option(
    "-n",
    "--name",
    type=str,
    required=True,
    help="需要同步的数据源名称",
)
def sync(name: str):
    context = DataAgent().run()
    datasource_repository = context.get_repository(StorageKey.DATASOURCE).convert(
        DatasourceRepository
    )
    item = datasource_repository.find_one(name)
    if item:
        if item.kind == Kind.MYSQL.value:
            mysql_conn = MysqlConnector(item, context)
            mysql_conn.query_schema()
    else:
        output_colored_text(f"执行失败, [{name}]数据源不存在", "error")


@datasource.command(help="查询当前已添加的数据源")
def ls():
    context = DataAgent(DataAgentKey.STORAGE).run()
    datasource_repository = context.get_repository(StorageKey.DATASOURCE).convert(
        DatasourceRepository
    )
    datasource_list = datasource_repository.ls()
    session.output.write("存在" + str(len(datasource_list)) + "个数据源")
    session.output.write("\n")
    for item in datasource_list:
        if item.enable:
            color = "enabled"
        else:
            color = "disabled"
        output_colored_text("========================", color)
        output_colored_text("名称：" + item.name, color)
        output_colored_text("地址：" + item.host, color)
        output_colored_text("端口：" + str(item.port), color)
        output_colored_text("数据源类型：" + str(item.kind), color)
        output_colored_text("数据库：" + str(item.database), color)
        output_colored_text("当前已选中：" + str(item.enable), color)
        output_colored_text("========================", color)


@datasource.command(help="删除已存在的数据源")
@click.option(
    "-n",
    "--name",
    type=str,
    required=True,
    help="数据源名称",
)
def delete(name: str):
    context = DataAgent(DataAgentKey.STORAGE).run()
    datasource_repository = context.get_repository(StorageKey.DATASOURCE)
    count = datasource_repository.delete(name)
    if count == 0:
        output_colored_text("删除成功", "success")
    else:
        output_colored_text(f"删除失败，[{name}]数据源不存在", "error")


@main.group()
def env():
    pass


@env.command()
@click.option(
    "-p",
    "--path",
    type=str,
    required=True,
    help=".env文件路径",
)
def load(path: str):
    import shutil

    if os.path.exists(path):
        shutil.copy(path, env_path)


@env.command()
def ls():
    import json

    print_formatted_text(
        FormattedText([("class:json", json.dumps(DataAgentEnv().__dict__, indent=4))])
    )


@main.group()
def log():
    pass


@log.command()
@click.option(
    "-p",
    "--path",
    type=str,
    required=True,
    help="log_config.yml文件路径",
)
def load(path: str):
    import shutil

    if os.path.exists(path):
        shutil.copy(path, log_path)


@log.command()
def ls():
    import json

    print_formatted_text(FormattedText([("class:json", json.dumps(log_config, indent=4))]))


if __name__ == "__main__":
    main()
