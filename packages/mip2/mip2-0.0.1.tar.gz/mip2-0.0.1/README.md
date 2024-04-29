# mip2

mip2 is a mip modeling tool that imitates gurobi's API syntax, making mip modeling easier.

The mip2 backend supports cbc, gurobi, scip, and copt solvers.

mip2 is not a re-implemented modeling tool, but is integrated based on py-mip, pyscipopt, coptpy and other tools. Therefore, when you need to use a specific solver, you need to install the corresponding tool package.

**CBC,GUROBI** 
```sh
pip install mip
```

**SCIP** 
```sh
conda install --channel conda-forge pyscipopt
```

**COPT** 
```sh
pip install coptpy
```


## examples
Here is a simple example.

```python

from mip2.api import Model, Param

m = Model(solver_name="CBC")
x = m.addVars([1,2,3], vtype="I", name="x")

m.addConstr(x[1] == 10)
m.addConstr(x.sum() <= 20)
m.addConstr(x.sum() >= 15)

m.setObjective(x.sum())
m.setParam(Param.MIPGap, 0.01)
m.setParam(Param.TimeLimit, 10)
status = m.optimize()

print("x value is:", [x[i].x for i in [1,2,3]])
print("obj value is:", m.objVal)
print("model status is:", status)
```



## api

