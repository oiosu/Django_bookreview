# ๐ Django_Book Review
![image](https://user-images.githubusercontent.com/99783474/199030424-b19938a6-15f2-4635-bcde-49a0a2fc8cc1.png)



## โ ๋ชฉํ
ํ์ด ํ๋ก๊ทธ๋๋ฐ์ ํตํ ์ฑ ๋ฆฌ๋ทฐ ์ปค๋ฎค๋ํฐ ์๋น์ค๋ฅผ ๊ฐ๋ฐํฉ๋๋ค. ์๋ ์กฐ๊ฑด์ ๋ง์กฑํด์ผ ํฉ๋๋ค.

- **CRUD** ๊ตฌํ(๊ตฌํ ๋ฐฉ๋ฒ ์ ํ ์์)
- **Staticfiles** ํ์ฉ ์ ์  ํ์ผ(์ด๋ฏธ์ง, CSS, JS) ๋ค๋ฃจ๊ธฐ
- Django **Auth** ํ์ฉ ํ์ ๊ด๋ฆฌ(ํ์ ๊ฐ์ / ํ์ ์กฐํ / ๋ก๊ทธ์ธ / ๋ก๊ทธ์์)
- Media ํ์ฉ ๋์  ํ์ผ ๋ค๋ฃจ๊ธฐ
- ๋ชจ๋ธ๊ฐ **1 : N / M : N ๊ด๊ณ** ๋งคํ

## โ ์๊ตฌ ์ฌํญ

### ๐ ๋ชจ๋ธ Model (๋ชจ๋ธ ์ด๋ฆ : User, ๋ชจ๋ธ ์ด๋ฆ : Review, ๋ชจ๋ธ ์ด๋ฆ : Comment)


### ๐ **ํผ Form** 

> `ํ์๊ฐ์`, `๋ก๊ทธ์ธ`, `๊ธฐ๋ฅ view`, `๋ฆฌ๋ทฐ reviews`, `๋ฐ์ดํฐ ์์ฑ`, `๋ฐ์ดํฐ ์์ `, `๋ฐ์ดํฐ ์ญ์ `

> ๋ฆฌ๋ทฐ `์ข์์ / ์ข์์ ์ทจ์`, `๋๊ธ comments`, `๋๊ธ ์์ฑ`, `๋๊ธ ์ญ์ `

> ํ์ ๊ด๋ฆฌ accounts `ํ์ ๊ฐ์`, `ํ์ ๋ชฉ๋ก ์กฐํ`, `ํ์ ์ ๋ณด ์กฐํ`, `๋ก๊ทธ์ธ`, `๋ก๊ทธ์์`, `ํ๋ก์ฐ`


### ๐ ํ๋ฉด Template

> `๋ฉ์ธ ํ์ด์ง`, `๋ชฉ๋ก ํ์ด์ง`, `๋ฆฌ๋ทฐ ์ ๋ณด ํ์ด์ง`, `๋ฆฌ๋ทฐ ์์ฑ ํ์ด์ง`, `๋ฆฌ๋ทฐ ์์  ํ์ด์ง`

> `ํ์ ๊ฐ์ ํ์ด์ง`, `ํ์ ์กฐํ ํ์ด์ง(ํ๋กํ ํ์ด์ง)`, `๋ก๊ทธ์ธ ํ์ด์ง`, `ํ๋ก์ฐ ๋ฒํผ`


---

### ๐ก ์ฃผ์ํ ์ 
#### โ ์๋ฌ ๋ฐ์ ๋ฌธ๊ตฌ : NoReverseMatch at /'accounts' is not a registered namespace

pjt ํด๋์ urls.py์์ path๋ฅผ 

```python
path('accounts/', include('allauth.urls')),
```

๋ก ์ค์ ํ์๋๋ ์๋ฌ๊ฐ ๋ฐ์
```python 
path("accounts/", include("accounts.urls")),
```
๋ก ์์ ํ์ฌ ํด๊ฒฐ

---

### โ ๋คํฌ ๋ชจ๋ ๊ธฐ๋ฅ ๊ตฌํ

![2022-10-31 23;32;43](https://user-images.githubusercontent.com/99783474/199033212-1bfd5d36-0c77-40a7-921d-1506f352bf4d.gif)

---

### โ ๋ฉ์ธ ํ์ด์ง 
![2022-10-31 23;35;30](https://user-images.githubusercontent.com/99783474/199033565-81abe824-acbf-4881-bf49-2753c31ab461.gif)

---

### โ ๋ก๊ทธ์ธ & ํ์ ๊ฐ์ 

![2022-10-31 23;37;48](https://user-images.githubusercontent.com/99783474/199034109-88ddb5ba-6930-4fe7-83eb-cd879d5f7370.gif)

![image](https://user-images.githubusercontent.com/99783474/199033636-32a0e0e9-f129-4aa4-ad21-a53fb848e475.png)

---

### โ ํ๋กํ
![image](https://user-images.githubusercontent.com/99783474/199034711-73fe2a5b-4b88-42df-85eb-2bb6213a957a.png)

---

### โ ๊ธ ๋ชฉ๋ก ํ์ด์ง 
![image](https://user-images.githubusercontent.com/99783474/199034945-e7195d14-0229-4257-b4b1-7b0a4285681d.png)



----

#### ์ฐธ์ฌ์๋ค
<a href="https://github.com/oiosu/Django_bookreview/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=oiosu/Django_bookreview" />
</a>

**๐ฉ ์ฐจํ์ ํ๊ณ ๋ก**
> ์ง๊ธ๊น์ง ๋ฐฐ์ด CRUD์ ๊ณผ์ ์ ํ์๊ด๋ฆฌ, ์ข์์ ๋ฐ ํ๋ก์ฐ ๊ธฐ๋ฅ์ ์ถ๊ฐํ์ฌ ์งํํ๋๋ฐ, ์์ง model ๊ฐ์ ๊ด๊ณ๋ฅผ ์๋ฒฝํ ์ดํดํ์ง ๋ชปํ์ง๋ง ํ๋ก์ ํธ๋ฅผ ํ๋ฉด์ ์กฐ๊ธ ์ ๋ฆฌ๊ฐ ๋์๋ค.  ์ฝ๋ ๋จ ๋ช ๊ธ์, ๋ช ์ค๋ก ์๊ธฐ๋ ์ค๋ฅ๋ฅผ ํจ๊ป ํด๊ฒฐํ๋ ๊ฒ์ด ๊ฑธ์ด์๋ ๊ธธ์ ๋๋์ ๊ฐ๋ ๊ฒ์ด๊ธฐ์ ์ฐธ ์์คํ ๊ฒฝํ์ ํ๋ค๊ณ  ์๊ฐํ๋ค. ๊ตฌํํ๋ฉด ํ ์๋ก ์์ฌ์ด ์๊ธฐ๊ณ , ํ๋ฉด ๊ตฌ์ฑ๊ณผ ๊พธ๋ฏธ๋ ๊ฒ์ ์ํ๋ ํ์ ๋๋ถ์ ๋ ์ด์ฌํ ํ  ์ ์์๋ค



**๐ฉ ์์๊ฒฝ ํ๊ณ ๋ก**
> ์ฅ๊ณ ๋ฅผ ํ๋ฒ ๋ ๋ณต์ตํ๋ฉด์ ์ฐจ๊ทผ์ฐจ๊ทผ ํ๋ก์ ํธ๋ฅผ ๋ง๋ค์ด ๊ฐ ์ ์์์ต๋๋ค. ๋ชจ๋ธ๊ฐ 1 : N / M : N ๊ด๊ณ๊ฐ ํนํ ์ดํดํ๊ธฐ ์ด๋ ค์ด ๋ถ๋ถ์ด์๋๋ฐ ํจ๊ป ์ฝ๋๋ฅผ ์์ฑํ๋ฉด์ ์ข์ ๊ฒฝํ์ ํ  ์ ์์์ต๋๋ค. ๋ค์์๋ ํผ๊ทธ๋ง์ ๋ ์์ธํ ์ด์ ์์ฑ์ ๋ ํด ๋๊ฐ๊ณ  ์ถ์ ์์ฌ์ด ์๊ฒผ์ต๋๋ค. 






