import guitarpro

hand_1 = {}
hand_1_counter = 0
hand_2 = {}
hand_2_counter = 0
leg_1 = {}
leg_1_counter = 0
leg_2 = {}
leg_2_counter = 0

def get_bps(tempo):
    return tempo/60

def get_average_hit_tempo(track):
    length_in_measures = len(track.measures)
    # for measure in track.measures:
        # measure.
    length_in_beats = track.measures


def beat_counter(track):
    hand_hits = 0
    leg_hits = 0
    for m in track.measures:
        if not m.isEmpty:
            for v in m.voices:
                if not v.isEmpty:
                    for b in v.beats:
                        for n in b.notes:
                            if n.value in LEGS_INSTRUMENTS:
                                leg_hits += 1
                            else:
                                hand_hits += 1
    print(f'Hits in track:\nLegs - {leg_hits}\nHands - {hand_hits}')
    return leg_hits, hand_hits


def instrument_limb_binding(voice):
    pass


LEGS_INSTRUMENTS = {
    44, 35, 36
}

INSTRUMENT_NAMES_MAP = {
    38: 'Snare(hit)',
    37: 'Snare(side stick)',
    91: 'Snare(rim shot)',
    42: 'HH (closed)',
    92: 'HH (half-open)',
    46: 'HH (open)',
    44: 'Pedal HH',
    35: 'Kick One',
    36: 'Kick Two',
    50: 'High Tom',
    48: 'High mid Tom',
    47: 'Mid Tom',
    45: 'Low Tom',
    43: 'Very Low Tom',
    93: 'Ride (edge)',
    51: 'Ride (mid)',
    53: 'Ride (bell)',
    55: 'Splash',
    52: 'China',
    49: 'High Crash',
    57: 'Mid Crash',
    99: 'Low Cowbell',
    56: 'Mid Cowbell',
    
}


demo = guitarpro.parse('acdc.gp4')
# print(demo.tracks)
bps = get_bps(demo.tempo)
# track_length = demo.
print(f'Tempo is {demo.tempo} bpm')
print(f'Tempo is {bps} bps')

for track in demo.tracks:
    if track.isPercussionTrack:
        print(f'Total measures: {len(track.measures)}')
        print(f'Drum track name: {track.name}')
        leg_beats, hand_beats = beat_counter(track)
        print()
        track_length = 0
        for measure in track.measures:
            track_length += measure.length

        print(track_length)
        # for measure in track.measures:
        #     print(measure.number)
        #     for voice in measure.voices:
        #         # if not voice.isEmpty:
        #
        #         for beat in voice.beats:
        #             print(beat.duration)
        #             # print(beat.status)
        #             # print(beat.display)
        #             print(beat.notes)
        #             for note in beat.notes:
        #                 print(note.value)

