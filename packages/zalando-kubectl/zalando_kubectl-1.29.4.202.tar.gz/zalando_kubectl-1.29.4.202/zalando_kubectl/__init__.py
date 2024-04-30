# This is replaced during release process.
__version_suffix__ = '202'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.29.4"
KUBECTL_SHA512 = {
    "linux": "c13235bd929eaaf4d0eaaa9ba883e95ce27a402ca7256c634e20a027fbf72db8834de8ea2ca7238e1fe92859e0edc7384a1cec7fbe2b7a5adf07b2e5cf99b04f",
    "darwin": "01506990cf76344fb12207e3e88a7c38a926ad8ccffc00b0ddcfeff9a5312b01438ef8c813e877e4b856cf1cc3f52dada7cd687a487797168a3436b66c64fc9b",
}
STERN_VERSION = "1.26.0"
STERN_SHA256 = {
    "linux": "de79474d9197582e38da0dccc8cd14af23d6b52b72bee06b62943c19ab95125e",
    "darwin": "f89631ea73659e1db4e9d8ef94c58cd2c4e92d595e5d2b7be9184f86e755ee95",
}
KUBELOGIN_VERSION = "v1.28.0"
KUBELOGIN_SHA256 = {
    "linux": "83282148fcc70ee32b46edb600c7e4232cbad02a56de6dc17e43e843fa55e89e",
    "darwin": "8169c6e85174a910f256cf21f08c4243a4fb54cd03a44e61b45129457219e646",
}
ZALANDO_AWS_CLI_VERSION = "0.4.3"
ZALANDO_AWS_CLI_SHA256 = {
    "linux": "bf0c32087985629c8694f4153230cbb7d627ae1794a942752f5cd1d76e118bf4",
    "darwin": "725d7262fb6c8e8705e1c3b59b53ccd78a59e9361711dc584b401d88cfd3fa69",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
