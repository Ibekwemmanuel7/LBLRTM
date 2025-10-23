clear variables;
close all;
fclose('all');
clc;
fs = 24;

% === Set folder path ===
currfolder = fullfile(pwd, '../data');
% === File paths and labels ===
files = {
    fullfile(currfolder, 'DomeC_means.txt'), ...     % Dome C Summer
    fullfile(currfolder, 'DomeC_meanw.txt'), ...     % Dome C Winter
    fullfile(currfolder, 'MZS_mean.txt'), ...        % MZS Summer
    fullfile(currfolder, 'MZSEra5w.txt')             % MZS Winter
};
labels = {'Dome C Summer', 'Dome C Winter', 'MZS Summer', 'MZS Winter'};

% Output base name for plots (no extension)
plotBase = fullfile(pwd, '../figures/Polar_Temp_WVMR_4Panel');
% Initialize data storage
height_all = cell(1, 4);
temp_all   = cell(1, 4);
wvmr_all   = cell(1, 4);

% Load data
for i = 1:numel(files)
    data = load(files{i});
    height_all{i} = data(:, 2);  % Height (km)
    temp_all{i}   = data(:, 4);  % Temperature (K)
    wvmr_all{i}   = data(:, 6);  % Water vapor VMR (ppmv)
end

% Axis ranges
height_range = [0, 16];
temp_range = [min(cellfun(@min, temp_all)), max(cellfun(@max, temp_all))];
wvmr_range = [min(cellfun(@min, wvmr_all)), max(cellfun(@max, wvmr_all))];

% Create figure
fig = figure('Position', [100, 100, 1200, 900], 'Color', 'white');
t = tiledlayout(2, 2, 'TileSpacing', 'compact', 'Padding', 'compact');

% Fonts
set(groot, 'defaultAxesFontName', 'Helvetica', 'defaultTextFontName', 'Helvetica');
set(groot, 'defaultAxesFontSize', 10, 'defaultTextFontSize', 10);

% Colors (colorblind-friendly)
colors = {[0.9, 0.3, 0.3], [0.3, 0.7, 0.3], [0.3, 0.3, 0.9], [0.7, 0.3, 0.7]};

% Panel (a): Summer Temperature
nexttile;
hold on;
plot(temp_all{1}, height_all{1}, 'Color', colors{1}, 'LineWidth', 2.5, ...
    'DisplayName', labels{1}, 'LineStyle', '-');
plot(temp_all{3}, height_all{3}, 'Color', colors{2}, 'LineWidth', 2.5, ...
    'DisplayName', labels{3}, 'LineStyle', '-');
xlabel('Temperature (K)', 'fontsize', fs);
ylabel('Height (km)', 'fontsize', fs);
text(0.02,0.95,'(a)','Units','normalized','FontSize',fs,'FontWeight','bold');
%title('(a)');
legend('show', 'Location', 'best', 'FontSize', fs, 'Box', 'off');
grid off; box on;
set(gca, 'XLim', temp_range, 'YLim', height_range, 'YTick', 0:4:16, 'fontsize', fs);

% Panel (b): Summer Water Vapor
nexttile;
hold on;
plot(wvmr_all{1}, height_all{1}, 'Color', colors{3}, 'LineWidth', 2.5, ...
    'DisplayName', labels{1}, 'LineStyle', '-');
plot(wvmr_all{3}, height_all{3}, 'Color', colors{4}, 'LineWidth', 2.5, ...
    'DisplayName', labels{3}, 'LineStyle', '-');
xlabel('WVMR (ppmv)', 'fontsize', fs);
ylabel('Height (km)', 'fontsize', fs);
text(0.02,0.95,'(b)','Units','normalized','FontSize',fs,'FontWeight','bold');
%title('(b)');
legend('show', 'Location', 'best', 'FontSize', fs, 'Box', 'off');
grid off; box on;
set(gca, 'YLim', height_range, 'YTick', 0:4:16, 'fontsize', fs);

% Panel (c): Winter Temperature
nexttile;
hold on;
plot(temp_all{2}, height_all{2}, 'Color', colors{1}, 'LineWidth', 2.5, ...
    'DisplayName', labels{2}, 'LineStyle', '-');
plot(temp_all{4}, height_all{4}, 'Color', colors{2}, 'LineWidth', 2.5, ...
    'DisplayName', labels{4}, 'LineStyle', '-');
xlabel('Temperature (K)', 'fontsize', fs);
ylabel('Height (km)', 'fontsize', fs);
text(0.02,0.95,'(c)','Units','normalized','FontSize',fs,'FontWeight','bold');
%title('(c)');
legend('show', 'Location', 'best', 'FontSize', fs, 'Box', 'off');
grid off; box on;
set(gca, 'XLim', temp_range, 'YLim', height_range, 'YTick', 0:4:16, 'fontsize', fs);

% Panel (d): Winter Water Vapor
nexttile;
hold on;
plot(wvmr_all{2}, height_all{2}, 'Color', colors{3}, 'LineWidth', 2.5, ...
    'DisplayName', labels{2}, 'LineStyle', '-');
plot(wvmr_all{4}, height_all{4}, 'Color', colors{4}, 'LineWidth', 2.5, ...
    'DisplayName', labels{4}, 'LineStyle', '-');
xlabel('WVMR (ppmv)', 'fontsize', fs);
ylabel('Height (km)', 'fontsize', fs);
%title('(d)');
legend('show', 'Location', 'best', 'FontSize', fs, 'Box', 'off');
grid off; box on;
set(gca, 'YLim', height_range, 'YTick', 0:4:16, 'fontsize', fs);
text(0.02,0.95,'(d)','Units','normalized','FontSize',fs,'FontWeight','bold');



% Save figures in multiple formats
print(fig, '-dtiff', '-r600', [plotBase, '.tiff']);     % High-quality TIFF
print(fig, '-depsc2', '-r600', [plotBase, '.eps']);     % EPS vector graphic
print(fig, '-dpng', '-r600', [plotBase, '.png']);       % Optional PNG

%disp(['Figure saved as: ', plotBase, '.{tiff, eps, png}']);
