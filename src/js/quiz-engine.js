/**
 * quiz-engine.js — 答题引擎
 * 管理答题状态：选项乱序、导航、答案存储。
 */

/**
 * Fisher-Yates 洗牌（带种子，确保同次答题顺序一致）
 */
function seededShuffle(arr, seed) {
  const a = [...arr];
  let s = seed;
  for (let i = a.length - 1; i > 0; i--) {
    // 简单的确定性伪随机
    s = (s * 16807 + 0) % 2147483647;
    const j = s % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/**
 * 创建答题引擎实例
 *
 * @param {Object[]} questions - 原始题目数组（来自 JSON）
 * @param {Object}   [opts]
 * @param {boolean}  [opts.shuffle=true]    - 是否随机打乱选项顺序
 * @param {number}   [opts.seed=Date.now()] - 随机种子（相同种子 = 相同顺序）
 * @returns {Object} engine API
 */
export function createQuizEngine(questions, opts = {}) {
  const shouldShuffle = opts.shuffle !== false;
  const seed = opts.seed ?? Date.now();

  // 预处理：为每道题生成乱序后的选项（保留原始 key，标签随内容走）
  const processed = questions.map((q) => {
    const originalOptions = q.options || [];

    if (shouldShuffle && originalOptions.length > 0) {
      const qSeed = seed + q.id * 31;
      const displayOptions = seededShuffle(originalOptions, qSeed);
      return {
        ...q,
        _displayOptions: displayOptions,
      };
    }

    return {
      ...q,
      _displayOptions: [...originalOptions],
    };
  });

  // ---- 状态 ----
  let _currentIndex = 0;
  // 用户答案：{ [questionId]: answerKey }  key 即选项标签（与原始一致）
  const _userAnswers = {};
  // 已锁定题目（已展示反馈）：Set<questionId>
  const _lockedQuestions = new Set();

  // ---- 内部工具 ----
  function _getQuestion(qId) {
    return processed.find((q) => q.id === qId);
  }

  // ---- 公开 API ----

  return {
    /** 获取当前题目索引 */
    get currentIndex() { return _currentIndex; },

    /** 获取题目总数 */
    get total() { return processed.length; },

    /** 获取已处理的题目列表（含 _displayOptions） */
    get questions() { return processed; },

    /** 获取用户全部答案（以原始 key 表示） */
    getUserAnswers() { return { ..._userAnswers }; },

    /** 获取已答题数 */
    getAnsweredCount() {
      return processed.filter((q) => {
        const a = _userAnswers[q.id];
        return a !== undefined && a !== null
          && (Array.isArray(a) ? a.length > 0 : true);
      }).length;
    },

    /** 获取当前题目的展示数据 */
    getCurrentQuestion() {
      const q = processed[_currentIndex];
      if (!q) return null;

      const userAnswer = _userAnswers[q.id];
      let selectedKeys;
      if (userAnswer === undefined || userAnswer === null) {
        selectedKeys = null;
      } else if (Array.isArray(userAnswer)) {
        selectedKeys = userAnswer;
      } else {
        selectedKeys = [userAnswer];
      }

      return {
        id: q.id,
        stem: q.stem,
        type: q.type,
        options: q._displayOptions,
        selectedKeys,
        isAnswered: userAnswer !== undefined && userAnswer !== null,
        index: _currentIndex,
        total: processed.length,
      };
    },

    /** 跳转到指定题目索引 */
    goTo(index) {
      if (index >= 0 && index < processed.length) {
        _currentIndex = index;
        return true;
      }
      return false;
    },

    /** 下一题 */
    next() {
      if (_currentIndex < processed.length - 1) {
        _currentIndex++;
        return true;
      }
      return false;
    },

    /** 上一题 */
    prev() {
      if (_currentIndex > 0) {
        _currentIndex--;
        return true;
      }
      return false;
    },

    /** 是否有上一题 */
    hasPrev() {
      return _currentIndex > 0;
    },

    /** 是否有下一题 */
    hasNext() {
      return _currentIndex < processed.length - 1;
    },

    /**
     * 选择答案
     * @param {number} questionId - 题目 ID
     * @param {string|string[]} displayKeys - 用户选择的显示 key（单选 "A" / 多选 ["A","C"]）
     */
    selectAnswer(questionId, keys) {
      if (keys === null || keys === undefined) {
        delete _userAnswers[questionId];
      } else {
        _userAnswers[questionId] = Array.isArray(keys) ? [...keys] : keys;
      }
    },

    /**
     * 清除某题的答案
     */
    clearAnswer(questionId) {
      delete _userAnswers[questionId];
    },

    /**
     * 锁定题目（展示反馈后调用，禁止修改答案）
     */
    lockQuestion(questionId) {
      _lockedQuestions.add(questionId);
    },

    /**
     * 题目是否已锁定
     */
    isLocked(questionId) {
      return _lockedQuestions.has(questionId);
    },

    /**
     * 获取已锁定题目数
     */
    getLockedCount() {
      return _lockedQuestions.size;
    },

    /**
     * 是否全部题目已锁定（即全部作答完毕）
     */
    isAllLocked() {
      return _lockedQuestions.size === processed.length;
    },

    /**
     * 重置引擎（清空答案，回到第一题）
     */
    reset() {
      _currentIndex = 0;
      for (const key in _userAnswers) {
        delete _userAnswers[key];
      }
      _lockedQuestions.clear();
    },

    /**
     * 检查是否全部题目已答
     */
    isAllAnswered() {
      return this.getAnsweredCount() === processed.length;
    },
  };
}
