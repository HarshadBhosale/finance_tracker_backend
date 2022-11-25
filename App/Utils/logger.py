def logger(func, params = {}):
    try:
        if params:
            return func(params)
        else:
            return func(**params)
    except Exception as error:
        with open('app.log', 'a') as log_file:
            error_message = 'Error: ' + str(error) + '\n\n'
            log_file.write(error_message)
        return { "message" : error_message }
