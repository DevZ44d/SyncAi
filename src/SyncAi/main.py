import requests
from importlib.metadata import version, PackageNotFoundError

class HackerGpt:
    """
    HackerGpt: A simple interface to interact with the SyncAi API
    for both chat-based prompts and image generation.
    """

    def __init__(self, api_key: str = "PyCodz"):
        self.api_key = api_key
        self.url = "https://dev-pycodz-blackbox.pantheonsite.io/DEvZ44d/Hacker.php"
        self.image_url = "https://dev-pycodz-blackbox.pantheonsite.io/DEvZ44d/imger.php?img="

    def prompt(self, request: str) -> str:
        """
        Send a text prompt to the HackerGpt API and return the response.
        """
        payload = {"text": request, "api_key": self.api_key}
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return f"[ERROR] Prompt failed: {e}"

    def generate_image(self, prompt: str, filename: str = None):
        """
        Generate an image using the provided prompt and save it locally.
        """
        try:
            response = requests.get(self.image_url + prompt)
            response.raise_for_status()
            file = filename or f"{prompt}.png"
            with open(file, "wb") as f:
                f.write(response.content)
            print(f"[INFO] Image saved as: {file}")
        except requests.RequestException as e:
            print(f"[ERROR] Image generation failed: {e}")

    def help(self) -> str:
        """
            Return usage instructions for the CLI.
        """
        return """
Usage: syncai -[OPTIONS] "[PROMPT]"

Options:
  -p,   --prompt     Start chatting with HackerGpt.
  -img, --imager     Generate an image from prompt.
  -h,   --help       Show this message and exit.
  -v,   --version    Show library version.
"""

    def version(self) -> str:
        """
            Return the version and author information for SyncAi.

            Returns:
                str: Formatted version string.
        """
        try:
            pkg_version = version("syncai")
        except PackageNotFoundError:
            pkg_version = "unknown"

        return f"SyncAi Version: {pkg_version}\nAuthor: PyCodz"

    @staticmethod
    def chat(prompt: str, api_key: str = "PyCodz") -> str:
        """
        Static shortcut to quickly send a prompt without manual instantiation.

        Args:
            prompt (str): The message to send to HackerGpt.
            api_key (str, optional): API key to use. Defaults to 'PyCodz'.

        Returns:
            str: Response from the server or an error message.
        """
        try:
            return HackerGpt(api_key=api_key).prompt(prompt)
        except Exception as e:
            return f"[ERROR] chat() failed: {e}"

