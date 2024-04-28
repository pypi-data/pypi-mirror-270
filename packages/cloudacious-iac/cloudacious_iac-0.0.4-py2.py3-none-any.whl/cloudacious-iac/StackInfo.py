from .Naming import Naming


class StackInfo:
    """
    Class that helps create, validate, and sift through the stack_info config.
    """

    def __init__(
        self,
        stack_info: dict,
    ):
        self.stack_info = stack_info

        self.stack_name: str = stack_info["stack_name"]
        self.client: str = stack_info["client_config"]["client"]
        self.container_registry_user: str = stack_info["container_registry_config"][
            "container_registry_user"
        ]
        self.container_registry_id: str = stack_info["container_registry_config"][
            "container_registry_id"
        ]
        self.container_repo: str = stack_info["container_registry_config"][
            "container_repo"
        ]

        return

    def image_config(self, fn_purpose) -> dict:
        """
        Given a stack_info with config for multiple functions, and therefore given the specific function, creates a dict with the information needed to create an image.
        """
        config: dict = self.stack_info["lambda_functions"][fn_purpose]

        target: str = config["dockerfile_target"]
        context: str = config["context"]
        build_args: dict = config["build_args"]
        dockerfile_name: str = config["dockerfile_name"]

        naming = Naming(stack_info=self.stack_info)
        self._image_name = naming.image_name(fn_purpose=fn_purpose)

        image_config: dict = {
            "stack_name": self.stack_name,
            "image_name": self._image_name,
            "target": target,
            "context": context,
            "build_args": build_args,
            "dockerfile_name": dockerfile_name,
            "container_registry_user": self.container_registry_user,
            "container_registry_id": self.container_registry_id,
            "container_repo": self.container_repo,
        }

        return image_config
