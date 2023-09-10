params = {'draw': '1'}
for index in range(0, 17):
    params[f'columns[{index}][data]'] = str(index)
    params[f'columns[{index}][name]'] = ''
    params[f'columns[{index}][searchable]'] = 'true'
    params[f'columns[{index}][orderable]'] = 'true'
    params[f'columns[{index}][search][value]'] = ''
    params[f'columns[{index}][search][regex]'] = 'false'
params['order[0][column]'] = '0'
params['order[0][dir]'] = 'asc' 
params['start'] = '0'           
params['length'] = '25'         
params['search[value]'] = ''    
params['search[regex]'] = 'false'
params['custom_order'] = 'popular'
params['token'] = ''            
params['___'] = 'default'       
