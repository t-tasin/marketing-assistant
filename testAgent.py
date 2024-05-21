import pkg_resources

try:
    pkg_resources.get_distribution('llama-index')
    print("LlamaIndex is installed")
except pkg_resources.DistributionNotFound:
    print("LlamaIndex is not installed")
