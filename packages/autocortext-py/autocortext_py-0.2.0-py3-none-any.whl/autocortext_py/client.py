import requests
import json


class AutoCortext:
    """
    A client for interacting with the AutoCortext API.

    This class provides methods to send messages and receive responses from the AutoCortext API.

    Attributes:
        org_id (str): The organization ID required for API requests.
        api_key (str): The API key used for secure communication with the API.
        base_url (str): The base URL for the API endpoints.
    """

    def __init__(self, org_id, api_key):
        """
        Initializes the AutoCortext client with necessary authentication credentials.

        Args:
            org_id (str): The organization ID for the API.
            api_key (str): The API key for accessing the API.

        Raises:
            ValueError: If either org_id or api_key is not provided.
        """
        if not org_id:
            raise ValueError("Organization ID must be provided and cannot be empty.")
        if not api_key:
            raise ValueError("API key must be provided and cannot be empty.")

        self.machine = "Not specified"
        self.verbosity = "concise"
        self.history = []
        self.base_url = "https://ascend-six.vercel.app/"
        self.org_id = org_id
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def troubleshoot(self, message):
        """
        Sends a troubleshooting message to the API and returns the response.

        The method expects a message in the form of a string or a dictionary and sends it
        as a JSON payload to the API's troubleshooting endpoint.

        Args:
            message (str or dict): The message or context to be sent for troubleshooting.

        Returns:
            str: The response from the API, typically containing troubleshooting information.

        Raises:
            ValueError: If the message is neither a string nor a dictionary.
            JSONDecodeError: If the response from the API is not valid JSON.
        """
        if isinstance(message, str):
            try:
                # Convert message to a Python dict if it's not already one
                print("[autocortext_py] Message is a string. Converting to JSON.")
                message = json.loads(message)
            except json.JSONDecodeError:
                raise ValueError("Message must be a valid JSON string or a dictionary.")

        # Add the message to the history (merge with existing history)
        self.history += message

        # Ensure message is a list of dicts
        if isinstance(message, list) and all(isinstance(m, dict) for m in message):
            # Find the highest current ID and add 1
            max_id = max(msg["id"] for msg in message) if message else 0

            if self.verbosity == "concise":
                # Add a message to keep responses concise
                print("[autocortext_py] consise mode selected")
                message.append(
                    {
                        "id": max_id + 1,
                        "content": "User: Also, please keep your response as short as possible.",
                        "role": "user",
                    }
                )
        else:
            raise ValueError(
                "Message must be a list of dictionaries with at least an 'id' key."
            )

        # Convert the list of messages into a single context string
        context = "\n".join(msg["content"] for msg in message)

        print("[autocortext_py] Sending context to server. Please wait...")
        response = requests.post(
            f"{self.base_url}/api/read?companyId={self.org_id}",
            headers=self.headers,
            json=context,
        )

        if response.status_code == 200:
            try:
                print("[autocortext_py] Response received. Processing...")
                response_data = response.json()
                content = response_data.get("data", "No data found")

                # Add the response to the history
                formatted_response = {
                    "id": max_id + 1,
                    "content": "Auto Cortext: " + content,
                    "role": "assistant",
                }

                self.history.append(formatted_response)
                return content

            except json.JSONDecodeError:
                return "Invalid JSON response"
        else:
            return f"Error: {response.status_code} - {response.text}"

    def set_verbosity(self, mode):
        """
        Set the verbosity of the AutoCortext client.

        The verbosity can be either "concise" or "verbose". In "concise" mode, AutoCortext will keep
        the response short and sweet. In "verbose" mode, AutoCortext will provide more detailed responses.

        Args:
            mode (str): The mode to set the client to. Must be either "concise" or "verbose".

        Raises:
            ValueError: If the mode is not a string or not "concise" or "verbose".
        """
        if not isinstance(mode, str):
            raise ValueError("Mode must be a string.")

        if mode not in ["concise", "verbose"]:
            raise ValueError("Mode must be either 'concise' or 'verbose'.")

        print(f"[autocortext_py] Verbosity set to {mode}.")
        self.verbosity = mode

    def set_machine(self, machine):
        """
        Set the machine name for the AutoCortext client.

        This method allows you to specify the name of the machine or system that is being troubleshooted.

        Args:
            machine (str): The name of the machine or system being troubleshooted.

        Returns:
            None

        Raises:
            ValueError: If the machine name is not provided or is not a string.
        """
        if not machine:
            raise ValueError("Machine name must be provided and cannot be empty.")

        if not isinstance(machine, str):
            raise ValueError("Machine name must be a string.")

        print(f"[autocortext_py] Machine set to {machine}.")
        self.machine = machine

    def save(self):
        """
        Save the history of messages exchanged with the AutoCortext API to a the remote server.

        This history will be viewable at https://ascend-six.vercel.app/dashboard/troubleshoot

        Args:
            None

        Returns:
            str: A message indicating the status of the save operation.
        """
        context = {
            "machine": self.machine,
            "messages": self.history,
            "companyId": self.org_id,
            "summarize": False,
        }

        print("[autocortext_py] Saving history to server. Please wait...")
        response = requests.post(
            f"{self.base_url}/api/history",
            headers=self.headers,
            json=context,
        )

        if response.status_code == 200:
            print("[autocortext_py] History saved successfully.")
            return "OK"
        else:
            return f"Error: {response.status_code} - {response.text}"
