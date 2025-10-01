import json

def proc_case(case):
    return {
        'input': case['messages'][1]['content'],
        'output': case['messages'][2]['content']
    }

if __name__ == '__main__':
    data = json.load(open('tim_long_box.json'))
    processed_data = [proc_case(case) for case in data]
    json.dump(processed_data, open('tim_long_box_processed.json', 'w'))