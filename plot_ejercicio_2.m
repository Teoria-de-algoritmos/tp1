




clear all
close all

time = [0.25 0.97 8.12 75.63 945.97];
samples = [1e1 1e2 1e3 1e4 1e5];



p = polyfit(samples,time,2);
y = polyval(p,samples);

str = ['Teórica: F(n) = ',num2str(p(1)),' n + ', num2str(p(2))];

figure(1)

scatter(samples, time,'Linewidth',4)
set(gca,'xscale','log')

hold on
plot(samples,y)






xgca = gca;
xgca.FontSize = 20;
title('Tarjan')
grid on
xlabel('Muestras')
ylabel('Tiempo [mS]')
legend('Mensurada',str)
ylim([0 max(time)])
