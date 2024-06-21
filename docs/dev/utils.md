### Cleanup
ВАЖНО: инструкция ниже - черновик, выполняйте команды только если понимаете что они делают и сделали бекап.

---

Может быть полезно удалить устаревшие файлы, которые теперь не используются - например, env и spp excel-файлы, картинки.

Пример, последовательности действий для удаления неиспользуемых env-файлов.

Зайти в django докер-контейнер
```bash
docker exec -it django19001-v2 bash
```

Зайти в шелл Django
```bash
python manage.py shell
```

Шелл работает как интерактивный Python.
Читаем файлы, которые физически есть в папке, сравниваем с теми, которые используются в модели, удаляем разницу.
```python
from apps.datasets.models import Dataset
import os

all_files = os.listdir('media/datasets/env/')

referenced_files = [i.env.path for i in Dataset.objects.all()]

to_delete_files = set(all_files) - set(referenced_files)

for i in to_delete_files:
    os.remove(i)
```
