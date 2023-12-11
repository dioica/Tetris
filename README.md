# Аттестационное тестирование
## Тест 1

# Блочное тестирование
## Б1 
Описание: test_grid_is_empty_true

Метод: is_empty(row, column)

Входные данные: grid[0][0] = 0, row = 0, column = 0

Ожидаемый результат: true

## Б2
Описание: test_grid_is_empty_false

Метод: is_empty(row, column)

Входные данные: grid[0][0] = 1, row = 0, column = 0

Ожидаемый результат: false

## Б3
Описание: test_grid_is_inside_true

Метод: is_inside(row, column)

Входные данные: 

```
row = 0, column = 0
row = 19, column = 0
row = 0, column = 9
row = 19, column = 9
row = 2, column = 7
```

Ожидаемый результат: 
```
true
true
true
true
true
```

## Б4 
Описание: test_grid_is_inside_false

Метод: is_inside(row, column)

Входные данные: 

```
row = -1, column = 0
row = 20, column = 0
row = 0, column = 10
row = 20, column = 10
```

Ожидаемый результат: 
```
false
false
false
false
```

## Б5 test_grid_is_row_full_true
Описание: Метод проверяет заполнены ли все клетки в строке, для случая, когда заполнены все клетки

0 строка поля полноcтью заполнена

Метод: is_row_full(row)

Входные данные: 
```
for i in range(num_cols):
  grid[0][i] = 1 
row = 0
```

Ожидаемый результат: true

## Б6 test_grid_is_row_full_false
Описание: Метод проверяет заполнены ли все клетки в строке для случая, когда заполнены не все клетки

В 1 строке закрашена 1 клетка, 0 строка полностью пустая

Метод: is_row_full(row)

Входные данные: 
```
grid[1][3] = 1
row = 0

row = 1
```

Ожидаемый результат: 
```
false
false
```

## Б7 test_grid_clear_row
Описание: Метод отчищает полностью заполненную строку

Метод: clear_row(row)

Входные даные:
```
for i in range(num_cols):
  grid[0][i] = 1 
row = 0
```
Ожидпемый результат:

Все значения клеток в 0 строке равны 0.
```
for i in range(num_cols):
  grid[0][i] == 0 
```

## Б8 test_grid_reset
Описание: Метод обнуляет значения всех клеток на поле

Метод: reset()

Входные даные:
```
for row in range(self.t_grid.num_rows - 5):
  for column in range(self.t_grid.num_cols - 2):
    self.t_grid.grid[row][column] = 1
```

Ожидаемый результат:
```
for row in range(self.t_grid.num_rows):
  for column in range(self.t_grid.num_cols):
    self.assertEqual(self.t_grid.grid[row][column], 0)
```


## Б9 test_grid_all_cells_above_are_empty_true
Описание: Метод проверяет пустые ли все клетки, над заданной клеткой, для случая, когда все клетки пустые

Метод: 
all_cells_above_are_empty(row, column)

Входные даные:
row = 5, column = 0

Ожидаемый результат:
true

## Б9 test_grid_all_cells_above_are_empty_false
Описание: Метод проверяет пустые ли все клетки, над заданной клеткой, для случая, когда не все клетки пустые

Метод: 
all_cells_above_are_empty(row, column)

Входные даные:
grid[5][6] = 1, row = 19, column = 5

Ожидаемый результат:
false

## Б10 test_grid_search_first_row_with_empty_cell_all_empty
Описание: Метод ищет первую строку хотя бы с одной пустой клеткой, для случая когда все клетки поля пустые

Метод: 
search_first_row_with_empty_cell()

Входные даные:

Ожидаемый результат: 
19

## Б11 test_grid_search_first_row_with_empty_cell_not_all_empty
Описание: Метод ищет первую строку хотя бы с одной пустой клеткой для случая, когда не все клетки поля пустые

Метод: 
search_first_row_with_empty_cell()

Входные даные:
```
for column in range(self.t_grid.num_cols - 1):
  self.t_grid.grid[19][column] = 1
self.t_grid.grid[18][9] = 1
```

Ожидаемый результат: 
18

## Б12 test_grid_search_empty_cells_all_empty
Описание: Метод ищет все пустые клетки для первых 2 строк с пустыми клетками для случая, когда все клтетки поля пустые

Метод: search_empty_cells()

Входные даные:

Ожидаемый результат: 
```
{19: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 18: []}
```

## Б12 test_grid_search_empty_cells_not_all_empty1
Описание: Метод ищет все пустые клетки для первых 2 строк с пустыми клетками для случая, когда не все клтетки поля пустые

Метод: search_empty_cells()

Входные даные:
```
grid[19][2] = 1
grid[18][9] = 1
```

Ожидаемый результат: 
```
{19: [0, 1, 3, 4, 5, 6, 7, 8], 18: [2]}
```

## Б13 test_grid_search_empty_cells_not_all_empty2
Описание: Метод ищет все пустые клетки для первых 2 строк с пустыми клетками для случая, когда не все клтетки пустые и 19 строка полностью заполнена

Метод: search_empty_cells()

Входные даные:
```
for column in range(num_cols):
  grid[19][column] = 1 
grid[18][9] = 1
```

Ожидаемый результат: 
```
{18: [0, 1, 2, 3, 4, 5, 6, 7, 8], 17: [9]}
```

## Б0
Описание:

Метод:

Входные даные:

Ожидаемый результат:



