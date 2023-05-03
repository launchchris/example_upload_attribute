# Import the LaunchDarkly client.
import ldclient
from ldclient import Context
from ldclient.config import Config

# Create a helper function for rendering messages.

def show_message(s):
    print("*** %s" % s)
    print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
    ldclient.set_config(Config("your_SDK_Key"))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
    show_message("SDK successfully initialized!")
else:
    show_message("SDK failed to initialize")
    exit()

# Set up the evaluation context. This context should appear on your LaunchDarkly contexts
# dashboard soon after you run the demo. Swap in the other values for other values
context = Context.builder("user-key-123abc").attribute_i_want("some_value").build()


# Call LaunchDarkly with the feature flag key you want to evaluate.
flag_value = ldclient.get().variation("some_flag_id", context, False)
