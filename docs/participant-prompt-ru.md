# Задание для @bySnach: 50 независимых вкладов в GitHub

Репозиторий: [vbysnach/open-source-micro-handbook](https://github.com/vbysnach/open-source-micro-handbook)

## Цель

Выполните все **50** лёгких документационных задач `DOC-01`–`DOC-50`. Это не олимпиадное программирование: каждая задача — завершить одну заранее подготовленную Markdown-карточку. Внутри файла уже есть опорный материал, поэтому не нужно искать информацию или устанавливать зависимости.

Требуется получить именно **50 новых содержательных commits автора `bySnach`** и **50 отдельных Pull Request** из вашего fork в `vbysnach/open-source-micro-handbook`. Начальная история fork и upstream в этот счёт не входит.

Для каждой задачи действует строгая схема:

- одна `DOC-XX` → одна ветка → один PR → один commit;
- один PR закрывает одну Issue и изменяет только назначенную карточку `cards/.../NN-...md`;
- все задачи `DOC-01`–`DOC-50` нужно выполнить ровно по одному разу — без пропусков и дубликатов.

## Где брать задачи

Откройте [Issues репозитория](https://github.com/vbysnach/open-source-micro-handbook/issues). Там опубликованы 50 открытых задач `DOC-01`–`DOC-50`. В каждой Issue указаны путь карточки и тема.

Не считайте, что номер Issue равен номеру `DOC`: в PR используйте фактический номер выбранной Issue в строке `Closes #<номер Issue>`.

Полный список карточек есть в [карте задач](task-cards.md).

## Настройка один раз

1. Сделайте fork репозитория в аккаунт `bySnach`.
2. Склонируйте свой fork и добавьте исходный репозиторий как `upstream`:

   ```bash
   git clone https://github.com/bySnach/open-source-micro-handbook.git
   cd open-source-micro-handbook
   git remote add upstream https://github.com/vbysnach/open-source-micro-handbook.git
   git fetch upstream
   ```

3. Убедитесь, что Git настроен на имя и верифицированный e-mail, привязанный к аккаунту `bySnach`; иначе вклад может не отобразиться в профиле:

   ```bash
   git config user.name
   git config user.email
   ```

## Как выполнить одну задачу

Повторите эти шаги для каждой из 50 Issue.

1. Выберите одну ещё не закрытую Issue `DOC-XX` и запомните её фактический номер.
2. Обновите ссылку на upstream и создайте отдельную ветку от `upstream/main`. Например, для `DOC-01`:

   ```bash
   git fetch upstream
   git switch -c docs/doc-01-clone upstream/main
   ```

3. Откройте **только** файл, указанный в Issue. Например: `cards/git/01-clone.md`.
4. В карточке:

   - замените `Статус: черновик` на `Статус: готово`;
   - заполните «Короткий ответ», «Шаги», «Частая ошибка» и «Мини-пример» по скрытому опорному материалу;
   - удалите HTML-комментарий с опорным материалом и все строки-заполнители.

5. При желании проверьте карточку локально:

   ```bash
   python scripts/validate_card.py cards/git/01-clone.md
   ```

   Для готовой карточки команда выводит `OK`.

6. Убедитесь, что изменён ровно один файл и в ветке будет ровно один commit:

   ```bash
   git diff --name-only
   git add cards/git/01-clone.md
   git commit -m "docs: DOC-01 complete clone card"
   git log upstream/main..HEAD --oneline
   git diff --name-only upstream/main...HEAD
   git push -u origin docs/doc-01-clone
   ```

   Перед push результат `git log` должен содержать один тематический `docs: DOC-XX ...` commit, а `git diff --name-only` — только назначенную карточку.

7. Откройте PR из вашей ветки в `vbysnach/open-source-micro-handbook:main`. Заголовок, например:

   ```text
   docs: DOC-01 — завершить карточку о клонировании
   ```

   В описание обязательно добавьте:

   ```text
   Closes #<фактический номер Issue>
   ```

## Обязательные ограничения

- Не изменяйте `README.md`, `docs/task-cards.md`, шаблоны GitHub, скрипты проверки, другие карточки или настройки репозитория.
- Не объединяйте несколько задач в один PR.
- Не закрывайте Issue вручную: её закроет `Closes #...` после merge PR.
- Не добавляйте второй commit при исправлении после ревью. Исправьте существующий commit и обновите ветку командой `git commit --amend`, затем `git push --force-with-lease`.

## Что будет после открытия PR

В репозитории намеренно нет GitHub Actions и обязательных status checks. Вы можете открыть **все 50 готовых PR подряд**, не ожидая `Approve and run`, CI, approval или merge предыдущих PR.

Ветка `main` защищена. Maintainer `vbysnach` проверит каждый маленький diff, оставит один approval и выполнит **Rebase and merge**. Вам не нужно и нельзя выполнять merge самостоятельно.

## Финальный чек-лист

- [ ] Открыты 50 PR: по одному для каждой `DOC-01`–`DOC-50`.
- [ ] Созданы ровно 50 новых commits `bySnach` с префиксом `docs: DOC-XX`.
- [ ] В каждом PR изменён только один назначенный файл.
- [ ] В каждом PR есть корректная строка `Closes #<номер Issue>`.
- [ ] В каждой карточке статус `готово`, все четыре раздела заполнены, а опорный HTML-комментарий удалён.

После этого сообщите maintainer’у, что все 50 PR открыты и готовы к ревью и rebase-merge.
