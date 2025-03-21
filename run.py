import importlib.metadata

from detquantlib.main import main

if __name__ == "__main__":
    # Print package name and version, as defined in pyproject.toml
    distribution_metadata = importlib.metadata.metadata("test_package_public")
    print(f">> {distribution_metadata['Name']} v.{distribution_metadata['Version']} <<")

    main()
