#### 1.用户认证的原理
* 首先，用户要能够输入用户名和密码，所以需要网页和表单，用以实现用户输入和提交的过程。

* 用户提交了用户名和密码，我们就需要比对用户名，密码是否正确，而要想比对，首先我们的系统中就要有存储用户名，密码的地方，大多数后台系统会通过数据库来存储，但是实际上我们也可以简单的存储到文件当中。(为简明起见，本文将用户信息存储到json文件当中)

* 登录之后，我们需要维持用户登录状态，以便用户在访问特定网页的时候来判断用户是否已经登录，以及是否有权限访问改网页。这就需要有维护一个会话来保存用户的登录状态和用户信息。
从第三步我们也可以看出，如果我们的网页需要权限保护，那么当请求到来的时候，我们就首先要检查用户的信息，比如是否已经登录，是否有权限等，如果检查通过，那么在response的时候就会将相应网页回复给请求的用户，但是如果检查不通过，那么就需要返回错误信息。

* 在第二步，我们知道要将用户名和密码存储起来，但是如果只是简单的用明文存储用户名和密码，很容易被“有心人”盗取，从而造成用户信息泄露，那么我们实际上应当将用户信息尤其是密码做加密处理之后再存储比较安全。

* 用户登出

#### 2.通过Flask以及相应的插件来实现登录过程
用到的插件
* flask-wtf
* wtf
* werkzeug
* flask_login

