# def swapList(arr: list) -> None:
#     n = len(arr)
#
#     for i in range(1, n, 2):
#         arr[i - 1], arr[i] = arr[i], arr[i - 1]
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def createLinkList(arr: list[int]) -> Node:
#     root = Node(arr[0])
#     curr = Node(0)
#     curr.next = root
#     curr = curr.next
#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         curr.next = temp
#         curr = curr.next
#
#     new_curr = root
#     while new_curr:
#         print(new_curr.data,'->',sep='', end='')
#         new_curr = new_curr.next
#
#     return root
#
#
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5]
#     root = createLinkList(arr)
#     # swapList(arr)
#     # print(arr)
#     #

def make_tag_push_cmd(list_of_images: list[str]) -> None:
    target_registry = "occne-repo-host:5000"
    for image_name in list_of_images:
        new_image_name = image_name.replace('localhost', target_registry)
        print(f"podman tag {image_name} {new_image_name}")
        print(f'podman push {new_image_name} --tls-verify=false')


def printTable(mystr):
    result = mystr.split('\n')

    for line in result:
        new_line = line.split(' ')
        # print(new_line)
        newer_line = [x for x in new_line if x!='']
        print('|'+'|'.join(newer_line)+'|')


if __name__=='__main__':
    target = '''
localhost/ocudr/nudr_datarepository_service:1.14.0
localhost/ocudr/nudr_post_rollback_hook:1.14.0
localhost/ocudr/nudr_bulk_import:1.14.0
localhost/ocudr/nudr_post_upgrade_hook:1.14.0
localhost/ocudr/readiness_check:1.14.0
localhost/ocudr/nudr_pre_migration_hook:1.14.0
localhost/ocudr/nudr_migration:1.14.0
localhost/ocudr/nudr_ondemand_migration:1.14.0
localhost/ocudr/nudr_pre_upgrade_hook:1.14.0
localhost/ocudr/nudr_pre_install_hook:1.14.0
localhost/ocudr/nudr_diameterproxy:1.14.0
localhost/ocudr/nudr_config:1.14.0
localhost/ocudr/nudr_notify_service:1.14.0
localhost/ocudr/diam-gateway:1.14.0
localhost/ocudr/ocingress_gateway:1.14.3
localhost/ocudr/ocegress_gateway:1.14.2
localhost/ocudr/nrf-client:1.8.0
localhost/ocudr/perf-info:1.14.0
localhost/ocudr/app-info:1.14.0
localhost/ocudr/ocpm_config_server:1.14.0
localhost/ocudr/common_config_hook:1.4.1
localhost/ocudr/configurationupdate:1.9.1
localhost/ocudr/configurationinit:1.9.1
localhost/ocudr/nf_test:1.14.1
localhost/ocudr/alternate_route:1.5.1
localhost/ocudr/debug-tools:1.1.0
localhost/ocudr/nudr_post_upgrade_hook:1.12.0
localhost/ocudr/readiness_check:1.12.0
localhost/ocudr/nudr_pre_migration_hook:1.12.0
localhost/ocudr/nudr_migration:1.12.0
localhost/ocudr/nudr_ondemand_migration:1.12.0
localhost/ocudr/nudr_pre_upgrade_hook:1.12.0
localhost/ocudr/nudr_bulk_import:1.12.0
localhost/ocudr/nudr_pre_install_hook:1.12.0
localhost/ocudr/nudr_diameterproxy:1.12.0
localhost/ocudr/nudr_config:1.12.0
localhost/ocudr/nudr_notify_service:1.12.0
localhost/ocudr/nudr_datarepository_service:1.12.0
localhost/ocudr/nudr_nrf_client_service:1.12.0
localhost/ocudr/perf-info:1.12.0
localhost/ocudr/ocpm_config_server:1.12.0
localhost/ocudr/alternate_route:1.4.2
localhost/ocudr/ocingress_gateway:1.12.2
localhost/ocudr/ocegress_gateway:1.12.2
localhost/ocudr/common_config_hook:1.3.2
localhost/ocudr/nf_test:1.12.0
localhost/ocudr/configurationupdate:1.8.0
localhost/ocudr/configurationinit:1.8.0
localhost/ocudr/debug-tools:1.10.0
localhost/ocudr/readiness-detector:1.12.0
    '''
    target_list = target.split('\n')
    make_tag_push_cmd(target_list)

    mystr = '''
NAME                                 REFERENCE                                       TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
ndbmgmd                              StatefulSet/ndbmgmd                             0%/80%    2         2         2          6d18h
ndbmtd                               StatefulSet/ndbmtd                              3%/80%    2         2         2          6d18h
ndbmysqld                            StatefulSet/ndbmysqld                           8%/80%    2         2         2          6d18h
nrf14-egressgateway-v1               Deployment/nrf14-egressgateway                  0%/80%    2         5         2          3d22h
nrf14-ingressgateway-v1              Deployment/nrf14-ingressgateway                 0%/80%    2         5         2          3d22h
nrf14-nfaccesstoken                  Deployment/nrf14-nfaccesstoken                  0%/80%    2         7         2          3d22h
nrf14-nfdiscovery                    Deployment/nrf14-nfdiscovery                    0%/80%    2         7         2          3d22h
nrf14-nfregistration                 Deployment/nrf14-nfregistration                 0%/80%    2         7         2          3d22h
nrf14-nfsubscription                 Deployment/nrf14-nfsubscription                 0%/80%    2         7         2          3d22h
nrf14-nrfconfiguration               Deployment/nrf14-nrfconfiguration               0%/80%    1         1         1          3d22h
ocudr-priyepan-egressgateway-v1      Deployment/ocudr-priyepan-egressgateway         0%/80%    1         4         1          2d
ocudr-priyepan-ingressgateway-v1     Deployment/ocudr-priyepan-ingressgateway        62%/80%   2         5         3          2d
ocudr-priyepan-nudr-config           Deployment/ocudr-priyepan-nudr-config           0%/80%    1         1         1          2d
ocudr-priyepan-nudr-diameterproxy    Deployment/ocudr-priyepan-nudr-diameterproxy    0%/80%    2         4         2          3d15h
ocudr-priyepan-nudr-drservice        Deployment/ocudr-priyepan-nudr-drservice        72%/80%   2         8         2          2d
ocudr-priyepan-nudr-notify-service   Deployment/ocudr-priyepan-nudr-notify-service   10%/80%   2         4         2          3d15h

NAME                                                      CPU(cores)   MEMORY(bytes)
mysql-cluster4-db-monitor-svc-6685bfddb9-6h95w            1m           237Mi
ndbmgmd-0                                                 4m           31Mi
ndbmgmd-1                                                 4m           28Mi
ndbmtd-0                                                  350m         13696Mi
ndbmtd-1                                                  401m         13688Mi
ndbmysqld-0                                               663m         756Mi
ndbmysqld-1                                               742m         723Mi
nrf14-appinfo-5747bd7c5c-h6gzh                            13m          246Mi
nrf14-egressgateway-fb8f9b79c-bfl9n                       2m           736Mi
nrf14-egressgateway-fb8f9b79c-p665f                       3m           596Mi
nrf14-ingressgateway-6c668965d9-c9tb9                     4m           826Mi
nrf14-ingressgateway-6c668965d9-tpb8l                     3m           1201Mi
nrf14-nfaccesstoken-748d687c8b-fdxtj                      2m           465Mi
nrf14-nfaccesstoken-748d687c8b-n5f7v                      1m           500Mi
nrf14-nfdiscovery-69c5dd547d-hk7pb                        1m           484Mi
nrf14-nfdiscovery-69c5dd547d-jhvb8                        2m           462Mi
nrf14-nfregistration-84c6bc4d89-b7qg6                     3m           597Mi
nrf14-nfregistration-84c6bc4d89-m9qfn                     3m           551Mi
nrf14-nfsubscription-784677dc88-stx4k                     2m           449Mi
nrf14-nfsubscription-784677dc88-xxxrr                     2m           469Mi
nrf14-nrfauditor-56b45dcc97-zzvv2                         4m           547Mi
nrf14-nrfconfiguration-5f8f9c6d7d-rhdc7                   3m           480Mi
ocudr-priyepan-egressgateway-6cf9bd46fc-ncbnw             2m           494Mi
ocudr-priyepan-ingressgateway-846765d9fc-42zfs            1863m        1455Mi
ocudr-priyepan-ingressgateway-846765d9fc-9ppbw            1943m        1121Mi
ocudr-priyepan-ingressgateway-846765d9fc-npwhr            3m           515Mi
ocudr-priyepan-nudr-config-869b978b-7l757                 2m           705Mi
ocudr-priyepan-nudr-config-server-7d5d474988-d6h5j        7m           395Mi
ocudr-priyepan-nudr-drservice-7fb8f855bb-5pxbz            1458m        826Mi
ocudr-priyepan-nudr-drservice-7fb8f855bb-lm7k6            1464m        705Mi
ocudr-priyepan-nudr-nrf-client-service-868c589bd4-qt2g7   1m           411Mi

    '''

    # printTable(mystr)
