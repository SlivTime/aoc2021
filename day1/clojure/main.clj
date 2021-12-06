(ns day-1
  (:require
   [clojure.string :as str]
   [clojure.test :refer [deftest is]]))

(def data-path "../input/input.txt")
(def test-data-path "../input/test_input.txt")
(def part-1-test-answer 7)
(def part-2-test-answer 5)

(defn get-data
  [file-path]
  (map read-string (str/split-lines (slurp file-path))))

(defn increasing?
  ([coll]
   (increasing? coll 1))
  ([coll window-size]
   (let [a (first coll)
         b (nth coll window-size nil)
         ok? (and (some? a) (some? b))]
     (if ok?
       (< a b)
       false))))

(defn do-count
  [data window-size]
  (loop [acc 0
         remaining data]
    (if (empty? remaining)
      acc
      (recur (if (increasing? remaining window-size) (+ acc 1) acc)
             (rest remaining)))))

(defn part-1
  [data]
  (do-count data 1))

(defn part-2
  [data]
  (do-count data 3))

(defn -main []
  (println (part-1 (get-data test-data-path)))
  (println (part-2 (get-data test-data-path)))
  (println (part-1 (get-data data-path)))
  (println (part-2 (get-data data-path))))

(-main)

(deftest test-part-1
  (is (=
       (part-1  (get-data test-data-path))
       part-1-test-answer)))

(deftest test-part-2
  (is (=
       (part-2  (get-data test-data-path))
       part-2-test-answer)))
