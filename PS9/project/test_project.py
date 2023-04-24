import pytest
import mock
import project
import events
import hud
from halfling import Halfling


def test_halfling():
    h = Halfling()

    # Test case for default values
    assert h.potatoes == 0
    assert h.destiny == 0
    assert h.orcs == 0
    assert h.danger_level == 1
    assert h.max_potatoes == 10
    assert h.max_destiny == 10
    assert h.max_orcs == 10

    # Test case for setters
    h.potatoes = 5
    assert h.potatoes == 5
    h.destiny = 8
    assert h.destiny == 8
    h.orcs = 3
    assert h.orcs == 3
    h.danger_level = 2
    assert h.danger_level == 2

    # Test case for reset function
    h.reset()
    assert h.potatoes == 0
    assert h.destiny == 0
    assert h.orcs == 0
    assert h.danger_level == 1


def test_title():
    assert project.title() == None
    # Test that title is printed without errors
    project.title()


def test_play():
    player = Halfling()
    # Test when user inputs 1
    with mock.patch("builtins.input", return_value="1"):
        assert project.play(player) == "1"
    # Test when user inputs 2
    with mock.patch("builtins.input", return_value="2"):
        assert project.play(player) == "2"
    # Test when user inputs 3
    with mock.patch("builtins.input", return_value="3"):
        assert project.play(player) == "3"


def test_play_again():
    player = Halfling()
    # Test when user inputs "y"
    with mock.patch("builtins.input", return_value="y"):
        assert project.play_again(player) == None

    # Test when user inputs "n"
    with mock.patch("builtins.input", return_value="n"):
        with pytest.raises(SystemExit):
            project.play_again(player)

    # Test when user inputs invalid input, then "n"
    with mock.patch("builtins.input", side_effect=["a", "n"]):
        with pytest.raises(SystemExit):
            project.play_again(player)


def test_project():
    print(project.title())


def test_events():
    assert events.roll() in range(1, 7)


def test_hud():
    print(hud.display(Halfling(), "basic"))
    print(hud.display(Halfling(), "minimal"))
    print(hud.display(Halfling(), "emoji"))
    print(hud.display(Halfling(), "fancy"))


def test_start():
    # Test case for choice 1
    with mock.patch("builtins.input", return_value="1"):
        assert project.start() == True

    # Test case for choice 2
    with mock.patch("builtins.input", return_value="2"):
        assert project.start() == False

    # Test case for invalid input
    with mock.patch("builtins.input", side_effect=["a", "2"]):
        assert project.start() == False


def test_game_loop():
    with mock.patch("builtins.input", return_value="1"):
        assert project.game_loop(Halfling(), "basic_interface") == None
