clear all
close all

time =   [6.39 9.07 26.81 62.26 245.37 3294.43 10440.27  27767.80 44400.698];
samples = [1e1 1e2 5e1   1e2  2e2 5e2       1e3   1.5e3   2e3];



p = polyfit(samples,time,2);
y = polyval(p,samples);

str = ['Teórica: F(n) = ',num2str(p(1)),' n^2 + ', num2str(p(2)),' n + ',num2str(p(3))];

figure(1)


scatter(samples, time,'Linewidth',4)

hold on
plot(samples,y)






xgca = gca;
xgca.FontSize = 20;
title('Gale Shapley')
grid on
xlabel('Muestras')
ylabel('Tiempo [mS]')
legend('Mensurada',str)
ylim([0 max(time)])
