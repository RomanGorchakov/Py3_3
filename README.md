Горчаков Роман Владимирович. Вариант 2
# Лабораторная работа 4.2. Перегрузка операторов в языке Python

Классы объявляются с помощью ключевого слова class и имени класса. Как правило, имя класса начинается с заглавной буквы и обычно является существительным или словосочетанием. Имена классов соответствуют соглашению CapWords (или UpperCamelCase): это означает, что если это фраза, все слова в этой фразе пишутся с большой буквы и пишутся без подчеркивания между ними.

Классы позволяют определять данные и поведение похожих объектов. Поведение описывается методами. Метод похож на функцию тем, что это блок кода, который имеет имя и выполняет определенное действие. Методы, однако, не являются независимыми, поскольку они определены внутри класса. Данные внутри классов хранятся в атрибутах (переменных), и их существует два вида: атрибуты класса и атрибуты экземпляра.

Атрибут класса - это атрибут, общий для всех экземпляров класса. Атрибуты класса определены внутри класса, но вне каких-либо методов. Их значения одинаковы для всех экземпляров этого класса. Так что вы можете рассматривать их как тип значений по умолчанию для всех наших объектов. Что касается переменных экземпляра, они хранят данные, уникальные для каждого объекта класса.

Экземпляр класса это то же самое, что и объект. Однако изначально все экземпляры класса будут идентичны друг другу. В большинстве случаев это не то, что нам требуется. И чтобы настроить начальное состояние экземпляра, используется метод __init__.

Метод __init__ является конструктором. Конструкторы - это концепция объектноориентированного программирования. Класс может иметь один и только один конструктор. Если __init__ определен внутри класса, он автоматически вызывается при создании нового экземпляра класса. Метод __init__ указывает, какие атрибуты будут у экземпляров нашего класса.

Аргумент self представляет конкретный экземпляр класса и позволяет нам получить доступ к его атрибутам и методам. Важно использовать параметр self внутри метода, если мы хотим сохранить значения экземпляра для последующего использования. В большинстве случаев нам также необходимо использовать параметр self в других методах, потому что при вызове метода первым аргументом, который ему передается, является сам объект. Параметр self (который представляет конкретный экземпляр класса) передается методу экземпляра неявно при его вызове. Таким образом, существует два способа вызова метода экземпляра: self.method () или class.method (self).

Атрибуты экземпляра определяются в методах и хранят информацию, специфичную для экземпляра. Обычно атрибуты экземпляра создаются в методе __init__, поскольку он является конструктором, но вы можете определить атрибуты экземпляра и в других методах. Атрибуты экземпляра, естественно, используются для различения объектов: их значения различны для разных экземпляров.

Атрибуты класса являются общими для всех объектов класса, а атрибуты экземпляра специфическими для каждого экземпляра. Более того, атрибуты класса определяются внутри класса, но вне каких-либо методов, а атрибуты экземпляра обычно определяются в методах, чаще всего в __init__. Несмотря на то, что все экземпляры имеют доступ к атрибуту класса, если эти атрибуты неизменны, изменение их значения для одного экземпляра не изменит их для всего класса.

Методы определяют функциональность объектов, принадлежащих конкретному классу. Параметры метода записаны в скобках. Первый параметр метода всегда должен быть self , так как self представляет конкретный экземпляр класса. Когда мы имеем дело с методами экземпляра, первым параметром, который передается методу, является объект, вызвавший его.

Хотя они очень похожи, в Python все же есть некоторые различия между методами и функциями. Естественно, основное отличие заключается в том, что методы являются частью структуры ООП, а функции - нет. Метод связан с объектом класса, он не является независимым, а вот функция является. Конечно, они оба вызываются по именам, но для вызова метода нам нужно вызвать также и класс, к которому принадлежит этот метод.

Атрибуты экземпляра - это как раз те, которые мы определяем в методах, поэтому по определению мы можем создавать новые атрибуты внутри наших пользовательских методов. Если атрибут имеет решающее значение для дальнейших вычислений, вы можете просто создать этот атрибут в методе __init__ и оставить создание необязательных атрибутов другим методам.

Если вы знакомы с языками программирования Java, C#, C++ то, наверное, уже задались вопросом: "а как управлять уровнем доступа?". В перечисленных языка вы можете явно указать для переменной, что доступ к ней снаружи класса запрещен, это делается с помощью ключевых слов (private, protected и т.д.). В Python таких возможностей нет, и любой может обратиться к атрибутам и методам вашего класса, если возникнет такая необходимость. Это существенный недостаток этого языка, т.к. нарушается один из ключевых принципов ООП – инкапсуляция. Хорошим тоном считается, что для чтения/изменения какого-то атрибута должны использоваться специальные методы, которые называются getter/setter, их можно реализовать, но ничего не помешает изменить атрибут напрямую. При этом есть соглашение, что метод или атрибут, который начинается с нижнего подчеркивания, является скрытым, и снаружи класса трогать его не нужно (хотя сделать это можно).

Свойством называется такой метод класса, работа с которым подобна работе с атрибутом. Для объявления метода свойством необходимо использовать декоратор @property . Важным преимуществом работы через свойства является то, что вы можете осуществлять проверку входных значений, перед тем как присвоить их атрибутам. Встроенная функция isinstance(obj, Cls), используемая при реализации методов арифметических операций и операций отношения, позволяет узнать что некоторый объект obj является либо экземпляром класса Cls либо экземпляром одного из потомков класса Cls.
