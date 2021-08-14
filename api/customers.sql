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