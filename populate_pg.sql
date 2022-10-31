create table backtests
(
	strategy varchar not null,
	timeframe varchar not null,
	pair varchar not null,
	state varchar,
	total_profits double precision,
	mean_profits double precision,
	trades_count integer,
	duration_avg varchar,
	wins integer,
	draws integer,
	losses integer,
	stats text,
	pnl text,
	asset_id varchar,
	constraint backtests_strategy_timeframe_pair_key
		unique (strategy, timeframe, pair)
);

alter table backtests owner to postgres;

create table stats
(
	asset_id varchar not null,
	creation_date date,
	loss_weeks_ratio double precision,
	active_weeks_count integer,
	active_weeks_ratio double precision,
	sharpe double precision,
	max_drawdown double precision,
	profit_weeks_ratio double precision,
	active_months_ratio double precision,
	active_months_count integer,
	volatility_daily double precision,
	weekly_returns varchar,
	win_to_loss_ratio double precision,
	daily_returns_mean double precision,
	monthly_returns_max double precision,
	weekly_returns_max double precision,
	profit_months_ratio double precision,
	volatility_weekly double precision,
	monthly_returns_std double precision,
	returns_cumsum varchar,
	daily_returns_max double precision,
	monthly_returns varchar,
	daily_returns_median double precision,
	monthly_returns_median double precision,
	weekly_returns_mean double precision,
	weekly_returns_median double precision,
	daily_returns_std double precision,
	loss_months_ratio double precision,
	monthly_returns_mean double precision,
	daily_returns varchar,
	daily_returns_min double precision,
	monthly_returns_min double precision,
	weekly_returns_min double precision,
	weekly_returns_std double precision,
	volatility_monthly double precision,
	stats_calculation_state varchar,
	duration_avg_stats varchar,
	with_watchdog boolean
);

alter table stats owner to postgres;

create unique index stats_asset_id_with_watchdog_uindex
	on stats (asset_id, with_watchdog);

create table trades
(
	pair varchar,
	stake_amount double precision,
	amount double precision,
	open_date varchar,
	close_date varchar,
	open_rate double precision,
	close_rate double precision,
	fee_open double precision,
	fee_close double precision,
	trade_duration varchar,
	profit_ratio double precision,
	profit_abs double precision,
	sell_reason varchar,
	initial_stop_loss_abs double precision,
	initial_stop_loss_ratio double precision,
	stop_loss_abs double precision,
	stop_loss_ratio double precision,
	min_rate double precision,
	max_rate double precision,
	is_open varchar,
	buy_tag varchar,
	open_timestamp varchar,
	close_timestamp varchar,
	asset_id varchar not null,
	trade_id varchar,
	watchdog_flag varchar,
	constraint trades_asset_id_open_timestamp_key
		unique (asset_id, open_timestamp)
);

alter table trades owner to postgres;

create table trading_watchdog_predictions
(
	trade_id varchar,
	watchdog_model varchar,
	watchdog_flag varchar,
	last_updated timestamp
);

alter table trading_watchdog_predictions owner to postgres;

create unique index trading_watchdog_trade_id_uindex
	on trading_watchdog_predictions (trade_id);

create table trading_watchdog_models
(
	model_name text,
	training_precision_score double precision,
	training_recall_score double precision,
	training_f1_score double precision,
	training_accuracy_score double precision,
	training_score double precision,
	val_precision_score double precision,
	val_recall_score double precision,
	val_f1_score double precision,
	val_accuracy_score double precision,
	val_score double precision,
	model_id text,
	run_id text,
	training_log_loss double precision,
	training_roc_auc_score double precision,
	best_cv_score double precision,
	val_log_loss double precision,
	val_roc_auc_score double precision
);

alter table trading_watchdog_models owner to postgres;

create index ix_quantdesk_schema_trading_watchdog_models_model_name
	on trading_watchdog_models (model_name);
