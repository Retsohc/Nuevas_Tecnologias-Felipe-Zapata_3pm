PGDMP  4                	    {            CarritoCompra    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    CarritoCompra    DATABASE     �   CREATE DATABASE "CarritoCompra" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "CarritoCompra";
                postgres    false            �            1259    16448    cart    TABLE     �   CREATE TABLE public.cart (
    cart_id integer NOT NULL,
    id_user integer NOT NULL,
    id_product integer NOT NULL,
    quantity integer NOT NULL,
    date_add timestamp(6) without time zone NOT NULL
);
    DROP TABLE public.cart;
       public         heap    postgres    false            �            1259    16447    cart_cart_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cart_cart_id_seq;
       public          postgres    false    220                        0    0    cart_cart_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart.cart_id;
          public          postgres    false    219            �            1259    16434    products    TABLE     �   CREATE TABLE public.products (
    product_id integer NOT NULL,
    name character varying(255) NOT NULL,
    price money NOT NULL,
    stock integer NOT NULL
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16433    product_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.product_product_id_seq;
       public          postgres    false    216                       0    0    product_product_id_seq    SEQUENCE OWNED BY     R   ALTER SEQUENCE public.product_product_id_seq OWNED BY public.products.product_id;
          public          postgres    false    215            �            1259    16441    users    TABLE     *  CREATE TABLE public.users (
    user_id integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(100) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(25) NOT NULL,
    registration_date timestamp(6) without time zone NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16440    users_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_user_id_seq;
       public          postgres    false    218                       0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
          public          postgres    false    217            \           2604    16451    cart cart_id    DEFAULT     l   ALTER TABLE ONLY public.cart ALTER COLUMN cart_id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);
 ;   ALTER TABLE public.cart ALTER COLUMN cart_id DROP DEFAULT;
       public          postgres    false    220    219    220            Z           2604    16437    products product_id    DEFAULT     y   ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.product_product_id_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    215    216    216            [           2604    16444    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    16448    cart 
   TABLE DATA           P   COPY public.cart (cart_id, id_user, id_product, quantity, date_add) FROM stdin;
    public          postgres    false    220   �       �          0    16434    products 
   TABLE DATA           B   COPY public.products (product_id, name, price, stock) FROM stdin;
    public          postgres    false    216   �       �          0    16441    users 
   TABLE DATA           \   COPY public.users (user_id, name, email, username, password, registration_date) FROM stdin;
    public          postgres    false    218   6                  0    0    cart_cart_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cart_cart_id_seq', 2, true);
          public          postgres    false    219                       0    0    product_product_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.product_product_id_seq', 15, true);
          public          postgres    false    215                       0    0    users_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_user_id_seq', 4, true);
          public          postgres    false    217            b           2606    16453    cart cart_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (cart_id);
 8   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_pkey;
       public            postgres    false    220            ^           2606    16439    products product_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.products
    ADD CONSTRAINT product_pkey PRIMARY KEY (product_id);
 ?   ALTER TABLE ONLY public.products DROP CONSTRAINT product_pkey;
       public            postgres    false    216            `           2606    16446    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    218            c           2606    16454    cart fk_products    FK CONSTRAINT     }   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT fk_products FOREIGN KEY (id_product) REFERENCES public.products(product_id);
 :   ALTER TABLE ONLY public.cart DROP CONSTRAINT fk_products;
       public          postgres    false    220    4702    216            d           2606    16459    cart fk_users    FK CONSTRAINT     q   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT fk_users FOREIGN KEY (id_user) REFERENCES public.users(user_id);
 7   ALTER TABLE ONLY public.cart DROP CONSTRAINT fk_users;
       public          postgres    false    220    218    4704            �   %   x�3�4�44FFƺ��F
V`����� ^Uj      �   p   x�34��MM�H��LV�N�L�O,J�T165�100�30�44�24��HML)N-QpO�M-�T1���p�r�;)���'q��!tZr��e�rJSK��K28UL���\1z\\\ P�H      �   o   x�3�-.M,���,��ɩ�)�zy�%@��"NC#cN##c]C]CK+0�2�tL����,.)JL�/�LD�!�415�j�	�z#��Fh0�462��52@����� ��6t     