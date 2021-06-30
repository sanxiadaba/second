clc,clear
syms x(t) t;
eqn=[diff(x)==0.132*x*(1-x),x(0)==0.4];
s=dsolve(eqn,t)