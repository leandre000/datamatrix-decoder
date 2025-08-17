try:
    result = future.result()
    results.append(result)
except Exception as e:
    logger.error(f'Error: {e}')

