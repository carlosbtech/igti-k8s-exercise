CREATE TABLE public.customers (
	id serial NOT NULL,
	nome text NULL,
	sexo text NULL,
	endereco text NULL,
	telefone text NULL,
	email text NULL,
	foto text NULL,
	nascimento date NULL,
	profissao text NULL,
	dt_update timestamp NULL,
	CONSTRAINT customers_pkey PRIMARY KEY (id)
);

CREATE TABLE public.flight (
	id serial NOT NULL,
	customer_id int NOT NULL,
	aeroporto text NULL,
	linha_aerea text NULL,
	cod_iata text NULL,
	dt_update timestamp NULL,
	CONSTRAINT flight_pkey PRIMARY KEY (id)
);

CREATE TABLE public.vehicle (
	id serial NOT NULL,
	customer_id int NOT NULL,
	ano_modelo text NULL,
	modelo text NULL,
	fabricante text NULL,
	ano_veiculo int4 NULL,
	categoria text NULL,
	dt_update timestamp NULL,
	CONSTRAINT vehicle_pkey PRIMARY KEY (id)
);