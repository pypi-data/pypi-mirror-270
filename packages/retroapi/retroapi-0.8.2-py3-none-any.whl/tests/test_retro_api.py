import pytest
from retroapi import RetroApi

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJndWVzdF93NmNkNDciLCJleHAiOjE3MDMyNTI3MjJ9.O6AMkE3Z8nHCmzEQDYpcbCP-wheD2ZRlXO2DSKSb904"

def test_valid_smiles():
    api = RetroApi(token)
    smiles = "COc1cccc(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    assert api.validate_smiles(smiles) is True
    smiles = "Cccccc1100(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    assert api.validate_smiles(smiles) is False


@pytest.mark.asyncio
async def test_avalid_smiles():
    api = RetroApi(token)
    smiles = "COc1cccc(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    res = await api.avalidate_smiles(smiles)
    assert res is True
    smiles = "Cccccc1100(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    res = await api.avalidate_smiles(smiles)
    assert res is False


def test_create_task():
    api = RetroApi(token)
    smiles = "COc1cccc(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    task_id = api.create_task(smiles)
    assert isinstance(task_id, str)
    routes = api.get_routes(task_id)
    if routes is not None:
        route = routes[0]
        assert 'plausibility' in route


@pytest.mark.asyncio
async def test_acreate_task():
    api = RetroApi(token)
    smiles = "COc1cccc(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"
    task_id = await api.acreate_task(smiles)
    assert isinstance(task_id, str)
    routes = await api.aget_routes(task_id)
    if routes is not None:
        route = routes[0]
        assert 'plausibility' in route


def test_image():
    api = RetroApi(token)
    # reaction
    # smiles = "CC(=O)OC(C)=O.COc1cc(C=O)cc(OC)c1OC>>COc1cc(C=CC(=O)O)cc(OC)c1OC"
    smiles = "COc1cc(C=CC(=O)O)cc(OC)c1OC"  # reagent
    img_bytes = api.get_image_from_smiles(smiles)
    assert isinstance(img_bytes, bytes)


@pytest.mark.asyncio
async def test_aimage():
    api = RetroApi(token)
    # reaction
    # smiles = "CC(=O)OC(C)=O.COc1cc(C=O)cc(OC)c1OC>>COc1cc(C=CC(=O)O)cc(OC)c1OC"
    smiles = "COc1cc(C=CC(=O)O)cc(OC)c1OC"  # reagent
    img_bytes = await api.aget_image_from_smiles(smiles)
    assert isinstance(img_bytes, bytes)


def test_synthesis_task():
    api = RetroApi(token)
    products = "COc1cc(C(=O)O)cc(OC)c1OC"
    reactants = "C=CC(=O)O.COc1cc(Br)cc(OC)c1OC"
    syn_task = api.create_syn_task(products, reactants)
    assert isinstance(syn_task, str)
    conditions = api.get_syn_conditions(syn_task)
    if conditions is not None:
        cond = conditions[0]
        assert "temperature" in cond
        assert "solvent" in cond


@pytest.mark.asyncio
async def test_asynthesis_task():
    api = RetroApi(token)
    products = "COc1cc(C(=O)O)cc(OC)c1OC"
    reactants = "C=CC(=O)O.COc1cc(Br)cc(OC)c1OC"
    syn_task = await api.acreate_syn_task(products, reactants)
    assert isinstance(syn_task, str)
    conditions = await api.aget_syn_conditions(syn_task)
    if conditions is not None:
        cond = conditions[0]
        assert "temperature" in cond
        assert "solvent" in cond
