
clear all
close all

time = [0.25077680212 1.75823438215 13.0119599093 141.123480073 1571.18099093 17790.6549749]
samples = [1e1 1e2 1e3 1e4 1e5 1e6]



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
title('Kosaraju')
grid on
xlabel('Muestras')
ylabel('Tiempo [mS]')
legend('Mensurada',str)
ylim([0 max(time)])