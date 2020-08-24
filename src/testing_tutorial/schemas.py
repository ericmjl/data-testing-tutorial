import pandera as pa
from pandera import Check, Column, DataFrameSchema

# Your answer goes here

positive_int_column = Column(
    pa.Int, checks=[Check.greater_than_or_equal_to(0)], nullable=False
)
bounded_zero_one_column = Column(
    pa.Float,
    checks=[Check.in_range(0, 1, include_min=True, include_max=True)],
    nullable=False,
)
positive_float_column = Column(
    pa.Float, checks=[Check.greater_than_or_equal_to(0)], nullable=False
)

boston_schema = DataFrameSchema(
    columns={
        "Year": Column(
            pa.Int, checks=[Check.isin([2013, 2014, 2015])], nullable=False
        ),
        "Month": Column(
            pa.Int, checks=[Check.isin(list(range(1, 13)))], nullable=False
        ),
        "logan_passengers": positive_int_column,
        "logan_intl_flights": positive_int_column,
        "hotel_occup_rate": bounded_zero_one_column,
        "hotel_avg_daily_rate": positive_float_column,
        "total_jobs": positive_int_column,
        "unemp_rate": bounded_zero_one_column,
        "labor_force_part_rate": bounded_zero_one_column,
        "pipeline_unit": positive_int_column,
        "pipeline_total_dev_cost": positive_int_column,
        "pipeline_sqft": positive_int_column,
        "pipeline_const_jobs": positive_float_column,
        "foreclosure_pet": positive_int_column,
        "foreclosure_deeds": positive_int_column,
        "med_housing_price": positive_int_column,
        "housing_sales_vol": positive_int_column,
        "new_housing_const_permits": positive_int_column,
        "new-affordable_housing_permits": positive_int_column,
    }
)



from pandas import Timestamp
from pandera import (
    DataFrameSchema,
    Column,
    Check,
    Index,
    MultiIndex,
    PandasDtype,
)

divvy_schema = DataFrameSchema(
    columns={
        "name": Column(
            pandas_dtype=PandasDtype.String, checks=None, nullable=False
        ),
        "latitude": Column(
            pandas_dtype=PandasDtype.Float64,
            checks=[
                Check.greater_than_or_equal_to(min_value=40),
                Check.less_than_or_equal_to(max_value=43),
            ],
            nullable=False,
        ),
        "longitude": Column(
            pandas_dtype=PandasDtype.Float64,
            checks=[
                Check.greater_than_or_equal_to(min_value=-89),
                Check.less_than_or_equal_to(max_value=-85),
            ],
            nullable=False,
        ),
        "dpcapacity": Column(
            pandas_dtype=PandasDtype.Int64,
            checks=[
                Check.greater_than_or_equal_to(min_value=0),
            ],
            nullable=False,
        ),
        "landmark": Column(
            pandas_dtype=PandasDtype.Int64,
            checks=[
                Check.greater_than_or_equal_to(min_value=0),
            ],
            nullable=False,
        ),
        "online_date": Column(
            pandas_dtype=PandasDtype.DateTime,
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=Timestamp("2013-06-28 00:00:00")
                ),
            ],
            nullable=False,
        ),
    },
    index=Index(
        pandas_dtype=PandasDtype.Int64,
        nullable=False,
        coerce=False,
        name="id",
    ),
    coerce=True,
    strict=False,
    name=None,
)