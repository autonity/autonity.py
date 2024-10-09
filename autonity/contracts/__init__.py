import warnings

# Suppress warnings raised by `plum` about not being able to resolve types
# from `eth_typing`; the dispatch works as expected
warnings.filterwarnings("ignore", message="Could not resolve the type hint")
warnings.filterwarnings("ignore", message="Could not determine whether .+ is faithful")
