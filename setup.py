import cx_Freeze

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name="Alien Invasion",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":['alien.py', 'bullet.py',
                                             'button.py', 'game_functions.py',
                                             'game_stats.py',
                                             'high_score.json', 'keys.py',
                                             'scoreboard.py', 'settings.py',
                                             'ship.py', 'images/abby.png',
                                             'images/background.jpg',
                                             'images/ship.png',
                                             'sound/bullet.wav',
                                             'sound/explosion.wav',
                                             'sound/hit.wav',
                                             'sound/level_up.wav',
                                             'sound/sad.mp3',
                                             'sound/stars.mp3']}},
    executables = executables

    )