import datetime
import json


def logs_decor(save_dir: str):
    def _logs_decor(old_func):
        def new_func(*args, **kwargs):
            log = {}
            date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            name = old_func.__name__
            result = old_func(*args, **kwargs)
            log['Время вызова функции'] = date_time
            log['Имя функции'] = name
            log['ARGS'] = args
            log['KWARGS'] = kwargs
            log['Возвращаемое значение'] = result
            with open(f'{save_dir}log.json', 'w', encoding='utf-8') as f:
                json.dump(log, f, ensure_ascii=False, indent=4)
            return result
        return new_func
    return _logs_decor

















