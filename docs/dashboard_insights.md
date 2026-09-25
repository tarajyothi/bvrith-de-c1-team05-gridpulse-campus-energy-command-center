# Dashboard Insights

**Week:** 9  
**Purpose:** Explain what the Power BI dashboard shows.

---

## 1. Dashboard Pages

| Page | Purpose | Main Visuals |
|---|---|---|
| Page 1: Campus Energy Overview | High-level view of campus energy consumption, cost and demand | KPI cards, daily energy trend, building comparison, peak demand and demand trend |
| Page 2: Building & Load Analysis | Building-level energy, demand, cost and intensity analysis | KPI cards, tariff cost chart, contributing meters, campus load profile, energy intensity |
| Page 3: Meter Health & Live Operations | Monitor meter readings, anomalies, completeness and operational health | KPI cards, anomaly trend, actual readings, reading completeness, power factor, meter status/type and health details |
| Week 10 Live Feed Placeholder | Reserved for future live meter-event monitoring | Live feed placeholder |

---

## 2. Key Insights

Write 5–8 insights from the dashboard.

1. The Campus Energy Overview provides a combined view of total energy consumption, estimated energy cost and campus demand, allowing overall campus performance to be monitored from one page.

2. The dashboard reports approximately **1.87K kWh** of total energy consumption and approximately **11.46K** in total estimated energy cost for the available selected data.

3. The available peak-load data shows a peak campus demand of approximately **6.25 kW**, while the demand trend shows how campus demand changes across measurement intervals.

4. The Building & Load Analysis page compares energy consumption across buildings and also provides energy intensity, allowing building usage to be considered relative to floor area.

5. The Energy Cost by Tariff Plan visual shows how estimated energy cost is distributed across the available tariff plans.

6. The Meter Health & Live Operations page reports **19 total anomaly readings** in the available anomaly data and provides a daily anomaly-rate trend for monitoring changes over time.

7. The dashboard reports approximately **96% reading completeness** based on actual readings compared with total available readings. This is a dashboard-derived completeness indicator and should not be treated as an independently calculated expected-interval metric.

8. Meter health visuals combine actual readings, estimated readings, average power factor, meter status and meter type to support operational monitoring and data-quality investigation.

---

## 3. How the Dashboard Uses Gold Tables

| Dashboard Page | Gold Table Used | Important Fields |
|---|---|---|
| Page 1: Campus Energy Overview | `agg_building_consumption_daily` | `date_key`, `building_id`, `total_energy_kwh`, `avg_active_power_kw` |
| Page 1: Campus Energy Overview | `agg_peak_load_interval` | `date_key`, `interval_ts`, `campus_demand_kw` |
| Page 1: Campus Energy Overview | `agg_energy_cost_daily` | `date_key`, `estimated_energy_cost` |
| Page 1: Campus Energy Overview | `dim_building` | `building_id`, `building_name` |
| Page 1: Campus Energy Overview | `dim_date` | `date_key` |
| Page 2: Building & Load Analysis | `agg_building_consumption_daily` | `building_id`, `date_key`, `total_energy_kwh`, `avg_active_power_kw` |
| Page 2: Building & Load Analysis | `agg_peak_load_interval` | `date_key`, `campus_demand_kw` |
| Page 2: Building & Load Analysis | `agg_energy_cost_daily` | `date_key`, `tariff_plan_id`, `estimated_energy_cost` |
| Page 2: Building & Load Analysis | `dim_building` | `building_id`, `building_name`, `floor_area_sqm` |
| Page 2: Building & Load Analysis | `dim_date` | `date_key` |
| Page 3: Meter Health & Live Operations | `agg_campus_anomaly_daily` | `date_key`, `total_readings`, `anomaly_reading_count`, `anomaly_rate` |
| Page 3: Meter Health & Live Operations | `agg_meter_health_daily` | `meter_id`, `building_id`, `date_key`, `reading_count`, `avg_power_factor`, `estimated_reading_count`, `actual_reading_count` |
| Page 3: Meter Health & Live Operations | `dim_meter` | `meter_id`, `building_id`, `meter_type`, `meter_status` |
| Page 3: Meter Health & Live Operations | `dim_building` | `building_id`, `building_name`, `campus_zone` |
| Page 3: Meter Health & Live Operations | `dim_date` | `date_key` |

---

### Validation Notes

The Power BI dashboard was refined using the existing Week 8 Gold-only model. Relationships were reviewed to avoid unnecessary direct joins between independent Gold summary tables.

The dashboard was tested using available Gold exports after Databricks access was unavailable during the refinement stage. Therefore, this documentation does not claim a new direct Databricks reconciliation during Week 9.

The dashboard values remain dependent on the available Gold data and the selected filter state.
