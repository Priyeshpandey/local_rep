inp = """
localhost/provgw/provgw_config:1.14.0
localhost/provgw/provgw_pre_upgrade_hook:1.14.0
localhost/provgw/provgw_pre_install_hook:1.14.0
localhost/provgw/auditor_service:1.14.0
localhost/provgw/provgw_service:1.14.0
localhost/provgw/readiness_check:1.14.0
localhost/provgw/ocingress_gateway:1.14.3
localhost/provgw/ocegress_gateway:1.14.2
localhost/provgw/ocpm_config_server:1.14.0
localhost/provgw/common_config_hook:1.4.1
localhost/provgw/configurationupdate:1.9.1
localhost/provgw/configurationinit:1.9.1
localhost/provgw/nf_test:1.14.1
localhost/provgw/debug-tools:1.1.0
"""

images = inp.split('\n')
cne_repo = "occne-repo-host:5000"
for image in images:
    print(f'podman untag {image}')
    # new_image = image.replace('localhost',cne_repo)
    # print(f'podman tag {image} {new_image}')
    # print(f'podman push {new_image} --tls-verify=false')