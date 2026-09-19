CREATE TABLE IF NOT EXISTS pipeline_watermark (
    pipeline_name VARCHAR(100) PRIMARY KEY,
    last_processed_date DATE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO pipeline_watermark (
    pipeline_name,
    last_processed_date
)
VALUES (
    'ecommerce_orders',
    NULL
)
ON CONFLICT (pipeline_name) DO NOTHING;