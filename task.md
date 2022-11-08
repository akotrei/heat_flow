Составьте программу (на Вашем любимом языке программирования) для численного решения
третьей краевой задачи для 1-мерного однородного нестационарного уравнения
теплопроводности в полярных координатах с постоянными коэффициентами. Теплообмен на
границах – по закону Ньютона – Рихмана, стационарный.

Входные данные:
R1, R2 – внутренний и внешний радиусы пространственной области (кольца), м;
delta_t – продолжительность прогнозного периода, с;
ro – плотность среды, кг / (м**3);
C_ro – удельная теплоемкость среды, Дж / (кг * К);
lambda – коэффициент теплопроводности среды, Вт / (м * К);
n – количество ячеек пространственной сетки (сетка – равномерная);
T_0i, (i = 0, ..., n) – начальные температуры среды в узлах сетки (i – номер узла; нумерация узлов – от 0 в
порядке увеличения радиуса), К;
a1, a2 – коэффициенты теплообмена на внутренней и внешней границах, Вт / (м**2 * К);
T1, T2 – температуры окружающей среды на внутренней и внешней границах, К.

Выходные данные:
T_i (i = 0, ..., n) – результирующие 1 температуры в узлах сетки, К.