clear all
close all

time = [0.25 0.97 8.12 75.63 945.97]
samples = [1e2 1e3 1e4 1e5 1e6]



k=0.0005;

figure(1)


scatter(samples, time,'Linewidth',4)
set(gca,'xscale','log')
hold on
plot(samples, k*(2*samples+1),'Linewidth',4)


str = ['Teórica: F(V,E) = ',num2str((k)),' * (V+E)'];



xgca = gca;
xgca.FontSize = 20;
title('Puntos de articulación')
grid on
xlabel('Muestras')
ylabel('Tiempo [mS]')
legend('Mensurada',str)

