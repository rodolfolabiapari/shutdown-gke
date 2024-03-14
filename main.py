#from google.cloud.container_v1 import ClusterManagerClient
#from kubernetes import client
#
#
#def test_gke(request):
#    project_id = "my-gcp-project"
#    zone = "my-zone"
#    cluster_id = "my-existing-cluster"
#
#    credentials = compute_engine.Credentials()
#
#    cluster_manager_client = ClusterManagerClient(credentials=credentials)
#    cluster = cluster_manager_client.get_cluster(name=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}')
#
#    configuration = client.Configuration()
#    configuration.host = f"https://{cluster.endpoint}:443"
#    configuration.verify_ssl = False
#    configuration.api_key = {"authorization": "Bearer " + credentials.token}
#    client.Configuration.set_default(configuration)
#
#    v1 = client.CoreV1Api()
#    print("Listing pods with their IPs:")
#    pods = v1.list_pod_for_all_namespaces(watch=False)
#    for i in pods.items:
#        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

from google.auth import compute_engine
from google.oauth2 import service_account
from google.cloud.container_v1 import ClusterManagerClient
#from kubernetes import client, config
#import os

def test_gke(project_id, zone, cluster_id):
    #SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    #credentials = service_account.Credentials.from_service_account_file(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'), scopes=SCOPES)

    credentials = compute_engine.Credentials()
    cluster_manager_client = ClusterManagerClient(credentials=credentials)

    cluster = cluster_manager_client.get_cluster(name=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}')

    print (cluster)
#    configuration = client.Configuration()
#    configuration.host = "https://"+cluster.endpoint+":443"
#    configuration.verify_ssl = False
#    configuration.api_key = {"authorization": "Bearer " + credentials.token}
#    client.Configuration.set_default(configuration)
#
#    v1 = client.CoreV1Api()
#    print("Listing pods with their IPs:")
#    pods = v1.list_pod_for_all_namespaces(watch=False)
#    for i in pods.items:
#        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

test_gke("prj-core-p-base-4980", "us-central1", "core-production")




from google.cloud.container_v1.types.cluster_service import SetNodePoolSizeRequest
from google.auth import compute_engine
from google.oauth2 import service_account
from google.cloud.container_v1 import ClusterManagerClient

def update_size_gke(project_id, zone, cluster_id, size):
    NODEPOOLS=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}/nodePools/ingress'
    credentials = compute_engine.Credentials()
    cluster_manager_client = ClusterManagerClient(credentials=credentials)

    #cluster = cluster_manager_client.get_cluster(name=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}')
    np = cluster_manager_client.list_node_pools(parent=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}')
    #print (np.node_pools())

    request = SetNodePoolSizeRequest(name=NODEPOOLS, node_count=size)
    cluster_manager_client.set_node_pool_size(request)

#    configuration = client.Configuration()
#    configuration.host = "https://"+cluster.endpoint+":443"
#    configuration.verify_ssl = False
#    configuration.api_key = {"authorization": "Bearer " + credentials.token}
#    client.Configuration.set_default(configuration)
#
#    v1 = client.CoreV1Api()
#    print("Listing pods with their IPs:")
#    pods = v1.list_pod_for_all_namespaces(watch=False)
#    for i in pods.items:
#        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

update_size_gke("prj-core-p-base-4980", "us-central1", "core-production", 0)