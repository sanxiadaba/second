syms x(t) y(t) t;
eqn=[diff(x)==y,diff(y)==-x,x(0)==-1,y(0)==2];
s=dsolve(eqn,t);
disp( s.x )
disp( s.y )
fplot(s.x,'ok-', 'linewidth', 1.5, 'markerfacecolor', [36, 169, 225]/255)
hold on;
fplot(s.y, 'ok-', 'linewidth', 1.5, 'markerfacecolor', [29, 191, 151]/255)
legend('x(t) = -5^(1/2)*cos(t + atan(2))','y(t) = 5^(1/2)*cos(t - atan(1/2))')
grid on
title('动力系统轨迹')
axis([-6, 3, -3 ,3])
set(gca, 'linewidth', 1.5, 'fontsize', 16, 'fontname', 'times')
xlabel('t')
ylabel('x(t)/y(t)')