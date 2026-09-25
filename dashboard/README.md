# Power BI Dashboard Folder

## Project

**Project:** GridPulse: Campus Energy Command Center  
**Team:** Team 05 – GridPulse

This folder contains the Power BI dashboard and documentation for the GridPulse campus energy reporting solution.

## Power BI Dashboard

The final Power BI file is maintained at:

`dashboard/powerbi_dashboard.pbix`

The dashboard is built using approved Gold-layer outputs only.

## Dashboard Pages

### Page 1 – Campus Energy Overview

This page provides a campus-level view of:

- Total energy consumption
- Total energy cost
- Peak campus demand
- Average demand
- Total buildings
- Daily energy consumption
- Energy consumption by building
- Daily peak campus demand
- Campus demand over time

The page includes date and building slicers for filtering the dashboard.

### Page 2 – Building & Load Analysis

This page provides building-level analysis of:

- Total energy consumption
- Peak campus demand
- Average demand
- Total energy cost
- Energy cost by tariff plan
- Contributing meters
- Campus load profile
- Energy intensity by building

The page includes building, tariff plan, time band, and date filters.

### Page 3 – Meter Health & Live Operations

This page provides operational monitoring of:

- Total anomaly readings
- Average anomaly rate
- Actual readings
- Total readings
- Reading completeness
- Daily anomaly rate
- Actual readings by building
- Meters by building
- Daily reading completeness
- Daily actual readings
- Average power factor by building
- Meter status distribution
- Meter type distribution
- Meter health details

A Week 10 live meter feed placeholder is included for future streaming integration.

## Gold Data Sources

The approved Gold-layer exports used for the dashboard are maintained in:

`data_sample/gold_exports/`

The Gold tables include:

- `agg_building_consumption_daily`
- `agg_peak_load_interval`
- `agg_energy_cost_daily`
- `agg_campus_anomaly_daily`
- `agg_meter_health_daily`
- `dim_building`
- `dim_date`
- `dim_meter`
- `dim_tariff`
- `dim_time_band`
- `fact_meter_reading`

Only the Gold outputs required by each dashboard page are used in that page's model.

## Power BI Measures

The main measures created for the dashboard include:

- **Total Energy (kWh)** – Sum of daily building energy consumption.
- **Average Demand (kW)** – Average active power demand.
- **Peak Campus Demand** – Maximum campus demand recorded in the selected data.
- **Total Energy Cost** – Sum of estimated energy cost.
- **Total Buildings** – Distinct count of buildings represented in the selected data.
- **Total Anomaly Readings** – Total anomaly readings from the campus anomaly Gold table.
- **Average Anomaly Rate** – Average anomaly rate from the campus anomaly Gold table.
- **Actual Readings** – Total actual meter readings.
- **Total Readings** – Total meter readings.
- **Reading Completeness** – Actual readings divided by total readings.

## Power BI Model

The dashboard uses dimensional relationships and Gold aggregated outputs.

Important model relationships include:

- `dim_date[date_key]` → `agg_building_consumption_daily[date_key]`
- `dim_date[date_key]` → `agg_peak_load_interval[date_key]`
- `dim_date[date_key]` → `agg_energy_cost_daily[date_key]`
- `dim_building[building_id]` → `agg_building_consumption_daily[building_id]`
- `dim_meter[meter_id]` → `agg_meter_health_daily[meter_id]`
- `dim_building[building_id]` → `dim_meter[building_id]`
- `dim_date[date_key]` → `agg_meter_health_daily[date_key]`
- `dim_date[date_key]` → `agg_campus_anomaly_daily[date_key]`

Relationships are designed as one-to-many relationships with single-direction filtering where appropriate.

Independent Gold summary tables are not directly joined merely because they contain similar fields.

## Week 08 Dashboard Foundation

Week 08 established the initial Power BI reporting foundation.

The work included:

- Loading approved Gold outputs into Power BI.
- Setting appropriate field types.
- Creating the required dimensional relationships.
- Creating the initial Power BI measures.
- Building the Campus Energy Overview page.
- Adding KPI cards and slicers.
- Adding energy, demand, cost, and building-level visuals.
- Checking slicer and visual behaviour.
- Documenting the Power BI hand-off.

The Week 08 Power BI hand-off notebook is:

`notebooks/06_powerbi_export.ipynb`

The Week 08 execution record is:

`weekly_logs/week08_log.md`

## Week 09 Dashboard Refinement

Week 09 continues from the Week 08 Power BI foundation.

The existing dashboard was refined through:

- Page-level visual refinement.
- Slicer and interaction testing.
- Building and load analysis.
- Meter health and operational analysis.
- Review of dashboard readability and visual hierarchy.
- Validation of important dashboard values against the available Gold outputs where applicable.
- Preparation of evidence-backed dashboard insights.

The Week 09 insight document is:

`docs/dashboard_insights.md`

The Week 09 execution record is:

`weekly_logs/week09_log.md`

## Evidence

Dashboard screenshots are stored in:

`screenshots/`

Week 08 evidence uses the `week08_` naming convention.

Week 09 evidence uses the `week09_` naming convention.

## Dashboard Data Rules

- Power BI must use approved Gold outputs only.
- Raw, Bronze, Silver, and quarantine data must not be used directly by dashboard visuals.
- Dashboard values must not be manually changed to produce desired results.
- Relationships must have a clear business and data-model purpose.
- KPI definitions should remain consistent with the approved Gold data.
- No unsupported KPI logic should be introduced when the required Gold data is unavailable.

## Power BI File-Size Rule

The preferred submission is the PBIX file together with dashboard screenshots.

If the `.pbix` file becomes too large to manage cleanly in GitHub, the final screenshots and dashboard documentation should remain in the repository, with a note explaining where the PBIX is stored for mentor review.

Multiple unnecessary PBIX versions should not be uploaded to the repository.
