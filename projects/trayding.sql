-- 1. Foydalanuvchilar jadvali (Users)
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    balance DECIMAL(18, 2) DEFAULT 0.00,
    currency VARCHAR(10) DEFAULT 'USD',
    account_status VARCHAR(20) DEFAULT 'active',
    verification_level INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Aktivlar jadvali (Assets/Instruments)
CREATE TABLE Assets (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
    ticker_symbol VARCHAR(10) NOT NULL UNIQUE,
    asset_name VARCHAR(100),
    asset_type VARCHAR(20), -- masalan: Crypto, Stock, Forex
    current_price DECIMAL(18, 8),
    daily_change_percent DECIMAL(5, 2),
    market_cap DECIMAL(20, 2),
    volume_24h DECIMAL(20, 2),
    is_tradable BOOLEAN DEFAULT TRUE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 3. Buyurtmalar jadvali (Orders)
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    asset_id INT,
    order_type VARCHAR(10), -- Buy yoki Sell
    order_category VARCHAR(20), -- Market, Limit, Stop
    quantity DECIMAL(18, 8),
    price_at_order DECIMAL(18, 8),
    total_amount DECIMAL(18, 2),
    order_status VARCHAR(20), -- Pending, Completed, Cancelled
    executed_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);

-- 4. Tranzaksiyalar tarixi jadvali (Transactions)
CREATE TABLE Transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_id INT,
    tx_type VARCHAR(20), -- Deposit, Withdrawal, Trade
    amount DECIMAL(18, 8),
    fee DECIMAL(10, 4),
    payment_method VARCHAR(50),
    tx_hash VARCHAR(100),
    tx_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);
