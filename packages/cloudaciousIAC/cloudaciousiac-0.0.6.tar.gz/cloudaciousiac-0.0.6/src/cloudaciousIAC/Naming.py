class Naming:
    def __init__(
        self,
        stack_info: dict,
    ):
        self.stack_info: dict = stack_info

        return

    def image_name(self, fn_purpose: str) -> str:
        """
        Given a properly formatted `stack_info` and the specified `fn_purpose` of the container, this method returns the image name that follows naming convention.
        """
        stack_name: str = self.stack_info["stack_name"].replace("_", "-")
        client: str = self.stack_info["client_config"]["client"]
        image_name: str = f"{stack_name}-{client}-{fn_purpose}"
        return image_name
