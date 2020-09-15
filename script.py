from dataclasses import dataclass
from dataclasses import dataclass
from typing import Any, Dict
from jinja2 import Template
import yaml
import os

@dataclass
class DefaultTemplater(object):
    """ Allow to inject data in a jinja2 templated file and write the result to specified destination """

    source: str
    destination: str
    template: str

    def __init__(self, source: str, destination: str) -> None:
        """ Args:
        source: source path of the template to load
        destination : where to write the final file
            """
        self.source = source
        self.destination = destination

    def render(self, data: Dict) -> None:
        """ Write template from source filled with data to destination
        Args:
        data: the data to inject in the template 

        """
        self.load_template()
        filled_template = self.replace(data)
        self.write_filled_template(filled_template)

    def load_template(self) -> None:
        """ Load template from source
        """
        with open(self.source, "r") as f:
            self.template = f.read()

    def replace(self, values: Dict) -> str:
        """ Replace tag in template with values
        Args: 
        values: dict with key: tag to search in template, value: value to replace the tag
        """
        template = Template(self.template)
        templated = template.render(**values)
        return templated

    def write_filled_template(self, content: str) -> None:
        """Write the result of the template and injected value to destination
        Args:
        content: what to write
        """
        with open(self.destination, "w") as f:
            f.write(content)


def template_webapp(config:Dict):
    """Template web app with according to config.yml file"""
    templater = DefaultTemplater("/template/Form.vue", "/app/src/views/Form.vue")
    tag = {"schema": config["schema"], "units": config["units"]}
    templater.render(tag)

    templater = DefaultTemplater("/template/Home.vue", "/app/src/views/Home.vue")
    tag = {"home": config["home"]}
    templater.render(tag)

    templater = DefaultTemplater("/template/App.vue", "/app/src/App.vue")
    tag = {"title": config["title"]}
    templater.render(tag)


if __name__ == "__main__":
    owner_repo = os.getenv("REPO")
    repo = owner_repo.split("/")[-1]
    os.environ["VUE_APP_GITHUB_PAGE"] = f"/{repo}/"
    with open("/form.yml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        template_webapp(config)