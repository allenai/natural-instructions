import json
import os
import uuid


tasks_path = 'tasks/'
files = [os.path.join(tasks_path, f) for f in os.listdir(tasks_path) if f.endswith('.json')]
files.sort()
for file in files: 
    print(file)
    task_id = os.path.basename(file).split('_')[0]
    with open(file) as f:
        data = json.load(f)
    for i, instance in enumerate(data['Instances']):
        data["Instances"][i] = {"id": task_id + '-' + uuid.uuid4().hex, **instance}
    with open(file, 'w') as fout:
        dump = json.dumps(data, indent = 4, ensure_ascii=False)
        fout.write(dump)


