import appstream_python
import pathlib


def _create_test_collection() -> appstream_python.AppstreamCollection:
    collection = appstream_python.AppstreamCollection()

    a_component = appstream_python.AppstreamComponent()
    a_component.id = "com.example.A"
    a_component.categories.append("Utility")
    collection.add_component(a_component)

    b_component = appstream_python.AppstreamComponent()
    b_component.id = "com.example.B"
    b_component.categories.append("Utility")
    b_component.categories.append("Game")
    collection.add_component(b_component)

    c_component = appstream_python.AppstreamComponent()
    c_component.id = "com.example.C"
    c_component.categories.append("Game")
    c_component.categories.append("System")
    collection.add_component(c_component)

    return collection


def test_collection_load_appstream_file() -> None:
    collection = appstream_python.AppstreamCollection()
    collection.load_appstream_file(pathlib.Path(__file__).parent / "data" / "AppStream" / "com.gitlab.JakobDev.jdTextEdit.metainfo.xml")
    assert collection.get_component("com.gitlab.JakobDev.jdTextEdit").id == "com.gitlab.JakobDev.jdTextEdit"
    assert len(collection) == 1


def test_collection_get_component_list() -> None:
    component_list = _create_test_collection().get_component_list()
    assert component_list[0].id == "com.example.A"
    assert component_list[1].id == "com.example.B"
    assert component_list[2].id == "com.example.C"
    assert len(component_list) == 3


def test_collection_get_component_id_list() -> None:
    assert _create_test_collection().get_component_id_list() == ["com.example.A", "com.example.B", "com.example.C"]


def test_collection_get_component() -> None:
    collection = _create_test_collection()
    assert collection.get_component("com.example.A").id == "com.example.A"
    assert collection.get_component("com.example.B").id == "com.example.B"
    assert collection.get_component("com.example.C").id == "com.example.C"
    assert collection.get_component("com.example.D") is None


def test_collection_find_by_category() -> None:
    collection = _create_test_collection()

    utility_list = collection.find_by_category("Utility")
    assert utility_list[0].id == "com.example.A"
    assert utility_list[1].id == "com.example.B"
    assert len(utility_list) == 2

    game_list = collection.find_by_category("Game")
    assert game_list[0].id == "com.example.B"
    assert game_list[1].id == "com.example.C"
    assert len(game_list) == 2

    system_list = collection.find_by_category("System")
    assert system_list[0].id == "com.example.C"
    assert len(system_list) == 1

    assert len(collection.find_by_category("Office")) == 0


def test_collection_write_load_uncompressed_collection(tmp_path: pathlib.Path) -> None:
    old_collection = _create_test_collection()
    old_collection.write_uncompressed_file(tmp_path / "test.xml")

    new_collection = appstream_python.AppstreamCollection()
    new_collection.load_uncompressed_appstream_collection(tmp_path / "test.xml")

    assert old_collection.get_component_id_list() == new_collection.get_component_id_list()


def test_collection_write_load_compressed_collection(tmp_path: pathlib.Path) -> None:
    old_collection = _create_test_collection()
    old_collection.write_compressed_file(tmp_path / "test.xml.gz")

    new_collection = appstream_python.AppstreamCollection()
    new_collection.load_compressed_appstream_collection(tmp_path / "test.xml.gz")

    assert old_collection.get_component_id_list() == new_collection.get_component_id_list()
