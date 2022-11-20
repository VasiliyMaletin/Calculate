import user_interface as ui
import calculation
import logger as log

def distribution():
    data = ui.expression()
    # calculation.init(data)
    if 'i' in data:
        result = calculation.calc_eval(data)
    else:
        result = calculation.calc(data)
    ui.view_result(result)
    log.expression_logger(data)
    log.result_logger(result)