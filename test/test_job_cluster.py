import random
import uuid

import pytest

import tator


def random_job_cluster_spec():
    uid = str(uuid.uuid4())
    return {
        "name": f"Job Cluster {uid}",
        "host": "test-host",
        "port": random.randint(4000, 6000),
        "token": uid,
        "cert": f"{uid}.cert",
    }

def test_job_cluster_crud(host, token, organization):
    tator_api = tator.get_api(host, token)
    user = tator_api.whoami()
    tator_api.create_affiliation(organization, {"permission": "Admin", "user": user.id})

    job_cluster_spec = random_job_cluster_spec()

    # Test creation
    response = tator_api.create_job_cluster(organization, job_cluster_spec)
    assert hasattr(response, "id")
    jc_id = response.id
    response = tator_api.get_job_cluster(jc_id)
    assert response.id == jc_id
    for k, v in job_cluster_spec.items():
        assert getattr(response, k) == v

    # Test read
    jc_list = tator_api.get_job_cluster_list(organization)
    assert len(jc_list) == 1
    job_cluster = jc_list[0]
    assert job_cluster.id == jc_id
    for k, v in job_cluster_spec.items():
        assert getattr(job_cluster, k) == v

    # Test update
    job_cluster_spec = random_job_cluster_spec()
    response = tator_api.update_job_cluster(jc_id, job_cluster_spec)
    assert response.message == f"Job Cluster {jc_id} successfully updated!"

    response = tator_api.get_job_cluster(jc_id)
    assert response.id == jc_id
    for k, v in job_cluster_spec.items():
        assert getattr(response, k) == v

    # Test delete
    response = tator_api.delete_job_cluster(jc_id)
    assert response.message == "Job cluster deleted successfully!"
    with pytest.raises(tator.openapi.tator_openapi.exceptions.ApiException):
        tator_api.get_job_cluster(jc_id)
