import tator

def test_analysis(
        host: str,
        token: str,
        project: int) -> None:
    """
    Create a set of analyses objects using the POST operation
    Retrieve the set of analyses objects
    Update the analysis object
    Get the object and make sure it was updated
    Delete the object
    Retrieve the set of analyses objects and make sure that object was deleted
    """

    # Setup the interface to tator
    tator_api = tator.get_api(host=host, token=token)

    # Create the analysis records
    name = "TestAnalysis"
    num_of_analyses = 10
    existing_num_of_analyses = len(tator_api.get_analysis_list(project=project))

    for count in range(num_of_analyses):
        data_query = f'random_query:{count}'
        spec = tator.models.AnalysisSpec(name=name, data_query=data_query)
        _ = tator_api.create_analysis(project=project, analysis_spec=spec)
        
    # Retrieve the analyses and verify the count matches
    analyses = tator_api.get_analysis_list(project=project)
    assert len(analyses) == existing_num_of_analyses + num_of_analyses

    # Update the analysis object
    obj = analyses[1]
    test_obj_id = obj.id
    spec = tator.models.Analysis(name="TestAnalysis2", data_query="another_random_query:0")
    _ = tator_api.update_analysis(id=test_obj_id, analysis_spec=spec)
    response = tator_api.get_analysis(id=test_obj_id)
    spec.id = test_obj_id
    assert response == spec

    # Remove the analysis object
    _ = tator_api.delete_analysis(id=test_obj_id)
    analyses = tator_api.get_analysis_list(project=project)
    analysis_is_gone = True
    for obj in analyses:
        if obj.id == test_obj_id:
            analysis_is_gone = False
            break 

    assert analysis_is_gone
    assert len(analyses) == existing_num_of_analyses + num_of_analyses - 1
