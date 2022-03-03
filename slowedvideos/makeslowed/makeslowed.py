def makeslowed(audio, howslow, output):

    prefix = 'Make Slowed Reverb -'

    from pedalboard import Pedalboard, VST3Plugin
    from pathlib import Path
    from math import trunc
    from os import remove
    import soundfile

    # Import audio file
    print(prefix, f'Importing {audio} ...')
    audio, sample_rate = soundfile.read(audio)

    # Slow audio
    print(prefix, 'Slowing audio...')
    sample_rate -= trunc(sample_rate*(howslow/100))

    # Add reverb (Path goes to the module and gets the full directory of TAL-Reverb-4.vst3)
    vst = VST3Plugin(str(Path(__file__).parent / "TAL-Reverb-4.vst3"))
    print(prefix, f'Adding reverb using {vst} ...')

    vst.size = 70
    vst.diffuse = 100
    vst.delay = '0.0000 s'
    vst.modulation_rate = 0
    vst.modulation_depth = 0
    vst.low_cut = 75
    vst.high_cut = 4000
    vst.dry = 80
    vst.wet = 25

    # Add effects
    effected = vst(audio, sample_rate)

    # Export audio
    print(prefix, f'Exporting audio as {output} ...')
    soundfile.write(output, effected, sample_rate)

    return print(prefix, 'Done')
